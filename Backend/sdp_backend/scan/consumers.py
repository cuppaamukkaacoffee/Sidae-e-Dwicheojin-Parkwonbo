import json as JSON
from channels.generic.websocket import AsyncWebsocketConsumer
from login.jwt import JwtHelper, AsyncJwtHelper
from rest_framework.response import Response
from rest_framework import status
import channels.exceptions
from .vuln import shmlackShmidow
from .spider import asyncCrawl
from .models import Reports
import asyncio
from aiohttp import ClientSession
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from .serializers import ReportsSerializer, RequestHeadersSerializer, ResponseHeadersSerializer, TargetsSerializer, CrawledUrlsSerializer
import hashlib


class ReportsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, message):
        await self.send(text_data=JSON.dumps({"message": message}))
        await self.close()
        raise channels.exceptions.StopConsumer

    async def receive(self, text_data):
        print(type(text_data))

        data_json = JSON.loads(text_data)
        jwt = AsyncJwtHelper()

        try:
            token = data_json["token"]
            target = data_json["target"]

            fuzz = data_json["fuzz"]

        except:
            print("nothing")
            await self.disconnect(message="missing body attribute")

        verification = await jwt.validate(token)
        print(verification)
        if not verification:
            await self.disconnect(message="invalid token")
        elif type(verification) == str:
            await self.disconnect(message=verification)

        if target:
            urlList = []
            session = ClientSession()
            async for url in asyncCrawl.crawl(target, session):
                urlList.append({"id": hashlib.md5((url + verification.username).encode("utf-8")).hexdigest(), "target": target, "url": url, "username": verification.username})
                await self.send(text_data=JSON.dumps({"status": "200", "urlList": url}))
            print("doing scan...")
            await session.close()

        if fuzz:
            tasks = []
            for url in urlList:
                session = ClientSession()
                task = asyncio.create_task(
                    shmlackShmidow.main(
                        url['url'], session=session, username=verification.username
                    )
                )
                tasks.append(task)

            for coro in asyncio.as_completed(tasks):
                reports, requests, responses = await asyncio.shield(coro)
                
                reports_serializers = ReportsSerializer(data=reports, many=True)
                requests_serializers = RequestHeadersSerializer(data=requests, many=True)
                responses_serializers = ResponseHeadersSerializer(data=responses, many=True)
                
                if await sync_to_async(reports_serializers.is_valid)(raise_exception=True) and \
                    await sync_to_async(requests_serializers.is_valid)(raise_exception=True) and \
                    await sync_to_async(responses_serializers.is_valid)(raise_exception=True):
                    await database_sync_to_async(reports_serializers.save)()
                    await database_sync_to_async(requests_serializers.save)()
                    await database_sync_to_async(responses_serializers.save)()
                
                # if requests_serializers.is_valid(raise_exception=True):
                #     await database_sync_to_async(requests_serializers.save)()
                
                # if responses_serializers.is_valid(raise_exception=True):
                #     await database_sync_to_async(responses_serializers.save)()

                result = {}
                result['reports'] = reports
                result['requests'] = requests
                result['responses'] = responses

                await self.send(text_data=JSON.dumps(result))
        
        targets_serializer = TargetsSerializer(data={"target": target, "username": verification.username})
        try:
            if await sync_to_async(targets_serializer.is_valid)(raise_exception=True):
                await database_sync_to_async(targets_serializer.save)()
        except:
            pass

        urls_serializer = CrawledUrlsSerializer(data=urlList, many=True)
        try:
            if await sync_to_async(urls_serializer.is_valid)(raise_exception=True):
                await database_sync_to_async(urls_serializer.save)()
        except Exception as e:
            # print(e)s
            pass

        await self.send(text_data=JSON.dumps({"status": "200"}))
        await self.disconnect(message="all good")
