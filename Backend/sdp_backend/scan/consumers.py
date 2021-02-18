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
from .serializers import ReportsSerializer


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

        result = []

        if target:
            urlList = await asyncCrawl.main(target)
            # print(urlList)
            await self.send(
                text_data=JSON.dumps({"status": "200", "urlList": list(urlList)})
            )
            print("doing scan...")

        if fuzz:
            async with ClientSession() as session:
                tasks = [asyncio.create_task(shmlackShmidow.main(
                        url, session=session, username=verification.username
                    )) for url in urlList]

                for coro in (asyncio.as_completed(tasks)):
                    result = await asyncio.shield(coro)
                    serializers = ReportsSerializer(data=result, many=True)
                    if serializers.is_valid(raise_exception=True):
                        await database_sync_to_async(serializers.save)()

                    await self.send(text_data=JSON.dumps({"result": result}))

        await self.send(text_data=JSON.dumps({"status": "200"}))
        await self.disconnect(message="all good")
