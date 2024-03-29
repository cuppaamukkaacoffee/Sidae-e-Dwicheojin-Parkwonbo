import json as JSON
from channels.generic.websocket import AsyncWebsocketConsumer
from login.jwt import JwtHelper, AsyncJwtHelper
from rest_framework.response import Response
from rest_framework import status
import channels.exceptions
from .vuln import shmlackShmidow, HeukGwabu, BaekGwabu, JeokGwabu
from .spider import asyncCrawl
from .models import Reports, Targets
import asyncio
from aiohttp import ClientSession
from asgiref.sync import sync_to_async
from channels.db import database_sync_to_async
from .serializers import (
    ReportsSerializer,
    RequestHeadersSerializer,
    ResponseHeadersSerializer,
    TargetsSerializer,
    CrawledUrlsSerializer,
)
import hashlib, datetime, random


class ReportsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, message):
        await self.send(text_data=JSON.dumps({"message": message}))
        await self.close()
        raise channels.exceptions.StopConsumer

    async def receive(self, text_data):
        random.seed(datetime.datetime.now())
        print(type(text_data))

        data_json = JSON.loads(text_data)
        jwt = AsyncJwtHelper()

        try:
            token = data_json["token"]
            target = data_json["target"]

            url_fuzz = data_json["url_fuzz"]
            form_fuzz = data_json["form_fuzz"]
            traversal_check = data_json["traversal_check"]

        except:
            print("nothing")
            await self.disconnect(message="missing body attribute")

        verification = await jwt.validate(token)
        print(verification)
        if not verification:
            await self.disconnect(message="invalid token")
        elif type(verification) == str:
            await self.disconnect(message=verification)

        scan_session_id = hashlib.md5(
            (str(random.random())).encode("utf-8")
        ).hexdigest()

        result_vulncount = {
            "SQL Injection": 0,
            "XSS": 0,
            "Open Redirect": 0,
            "Windows Directory Traversal": 0,
            "Linux Directory Traversal": 0,
            "LFI Check": 0,
            "RFI Check": 0,
            "RCE Linux Check": 0,
            "RCE PHP Check": 0,
            "SSTI Check": 0,
        }

        if target:
            if target[-1] != "/":
                target += "/"
            urlList = []
            session = ClientSession()
            async for url in asyncCrawl.crawl(target, session):
                urlList.append(
                    {
                        "id": hashlib.md5(
                            (url + verification.username).encode("utf-8")
                        ).hexdigest(),
                        "scan_session_id": scan_session_id,
                        "target": target,
                        "url": url,
                        "username": verification.username,
                    }
                )
                await self.send(text_data=JSON.dumps({"status": "200", "urlList": url}))
            _urlLists = [urlList]
            if len(urlList) > 30:
                print(f"length of urslList: {len(urlList)}")
                _urlLists = []
                for i in range(int(len(urlList) / 30) + 1):
                    front = i * 30
                    back = (i + 1) * 30
                    if back > len(urlList):
                        back = len(urlList)
                    _urlLists.append(urlList[front:back])
            print("doing scan...")
            await session.close()

        if url_fuzz:
            await self.send(text_data=JSON.dumps({"message": "doing url fuzz..."}))
            for _urlList in _urlLists:
                tasks = []
                for url in _urlList:
                    session = ClientSession()
                    task = asyncio.create_task(
                        # shmlackShmidow.main(
                        #     url['url'], session=session, username=verification.username, scan_session_id=scan_session_id
                        # )
                        HeukGwabu.main(
                            url["url"],
                            session=session,
                            username=verification.username,
                            scan_session_id=scan_session_id,
                        )
                    )
                    tasks.append(task)

                for coro in asyncio.as_completed(tasks):
                    reports, requests, responses, vulncount = await asyncio.shield(coro)

                    result_vulncount["SQL Injection"] += vulncount["SQL Injection"]
                    result_vulncount["XSS"] += vulncount["XSS"]
                    result_vulncount["Open Redirect"] += vulncount["Open Redirect"]
                    result_vulncount["Windows Directory Traversal"] += vulncount[
                        "Windows Directory Traversal"
                    ]
                    result_vulncount["Linux Directory Traversal"] += vulncount[
                        "Linux Directory Traversal"
                    ]
                    result_vulncount["LFI Check"] += vulncount["LFI Check"]
                    result_vulncount["RFI Check"] += vulncount["RFI Check"]
                    result_vulncount["RCE Linux Check"] += vulncount["RCE Linux Check"]
                    result_vulncount["RCE PHP Check"] += vulncount["RCE PHP Check"]
                    result_vulncount["SSTI Check"] += vulncount["SSTI Check"]

                    reports_serializers = ReportsSerializer(data=reports, many=True)
                    requests_serializers = RequestHeadersSerializer(
                        data=requests, many=True
                    )
                    responses_serializers = ResponseHeadersSerializer(
                        data=responses, many=True
                    )
                    try:
                        if (
                            await sync_to_async(reports_serializers.is_valid)(
                                raise_exception=True
                            )
                            and await sync_to_async(requests_serializers.is_valid)(
                                raise_exception=True
                            )
                            and await sync_to_async(responses_serializers.is_valid)(
                                raise_exception=True
                            )
                        ):
                            await database_sync_to_async(reports_serializers.save)()
                            await database_sync_to_async(requests_serializers.save)()
                            await database_sync_to_async(responses_serializers.save)()
                    except Exception as e:
                        print(e)
                        for report in reports:
                            print(f"id: {report['id']} url: {report['url']} vulon: {report['vulnerability']}")

                    # if requests_serializers.is_valid(raise_exception=True):
                    #     await database_sync_to_async(requests_serializers.save)()

                    # if responses_serializers.is_valid(raise_exception=True):
                    #     await database_sync_to_async(responses_serializers.save)()

                    result = {}
                    result["reports"] = reports
                    result["requests"] = requests
                    result["responses"] = responses

                    await self.send(text_data=JSON.dumps(result))

        if form_fuzz:
            print("doing form fuzz")
            await self.send(text_data=JSON.dumps({"message": "doing form fuzz..."}))
            for _urlList in _urlLists:
                tasks = []
                for url in _urlList:
                    session = ClientSession()
                    task = asyncio.create_task(
                        # shmlackShmidow.main(
                        #     url['url'], session=session, username=verification.username, scan_session_id=scan_session_id
                        # )
                        JeokGwabu.main(
                            url=url["url"],
                            session=session,
                            username=verification.username,
                            scan_session_id=scan_session_id,
                        )
                    )
                    tasks.append(task)

                for coro in asyncio.as_completed(tasks):
                    reports, requests, responses, vulncount = await asyncio.shield(coro)
                    if reports == [] and requests == [] and responses == []:
                        print("empty received")
                        continue
                    result_vulncount["SQL Injection"] += vulncount["SQL Injection"]
                    result_vulncount["XSS"] += vulncount["XSS"]

                    reports_serializers = ReportsSerializer(data=reports, many=True)
                    requests_serializers = RequestHeadersSerializer(
                        data=requests, many=True
                    )
                    responses_serializers = ResponseHeadersSerializer(
                        data=responses, many=True
                    )

                    if (
                        await sync_to_async(reports_serializers.is_valid)(
                            raise_exception=True
                        )
                        and await sync_to_async(requests_serializers.is_valid)(
                            raise_exception=True
                        )
                        and await sync_to_async(responses_serializers.is_valid)(
                            raise_exception=True
                        )
                    ):
                        await database_sync_to_async(reports_serializers.save)()
                        await database_sync_to_async(requests_serializers.save)()
                        await database_sync_to_async(responses_serializers.save)()

                    # if requests_serializers.is_valid(raise_exception=True):
                    #     await database_sync_to_async(requests_serializers.save)()

                    # if responses_serializers.is_valid(raise_exception=True):
                    #     await database_sync_to_async(responses_serializers.save)()

                    result = {}
                    result["reports"] = reports
                    result["requests"] = requests
                    result["responses"] = responses

                    await self.send(text_data=JSON.dumps(result))

        if traversal_check:
            await self.send(text_data=JSON.dumps({"message": "doing traversal check..."}))
            print("at traversal")
            session = ClientSession()
            reports, requests, responses, count = await asyncio.shield(
                BaekGwabu.main(
                    target=target,
                    session=session,
                    username=verification.username,
                    scan_session_id=scan_session_id,
                )
            )

            print("trav scan done")

            if count != 0:
                result_vulncount["Linux Directory Traversal"] += count

                reports_serializers = ReportsSerializer(data=reports, many=True)
                requests_serializers = RequestHeadersSerializer(
                    data=requests, many=True
                )
                responses_serializers = ResponseHeadersSerializer(
                    data=responses, many=True
                )

                if (
                    await sync_to_async(reports_serializers.is_valid)(
                        raise_exception=True
                    )
                    and await sync_to_async(requests_serializers.is_valid)(
                        raise_exception=True
                    )
                    and await sync_to_async(responses_serializers.is_valid)(
                        raise_exception=True
                    )
                ):
                    await database_sync_to_async(reports_serializers.save)()
                    await database_sync_to_async(requests_serializers.save)()
                    await database_sync_to_async(responses_serializers.save)()

                # if requests_serializers.is_valid(raise_exception=True):
                #     await database_sync_to_async(requests_serializers.save)()

                # if responses_serializers.is_valid(raise_exception=True):
                #     await database_sync_to_async(responses_serializers.save)()

                result = {}
                result["reports"] = reports
                result["requests"] = requests
                result["responses"] = responses

                await self.send(text_data=JSON.dumps(result))

            else:
                await self.send(
                    text_data=JSON.dumps(
                        {"traversal_result": "no traversal vulnerbility detected"}
                    )
                )

        target_data = {
            "id": scan_session_id,
            "target": target,
            "username": verification.username,
            "sqli": result_vulncount["SQL Injection"],
            "xss": result_vulncount["XSS"],
            "open_redirect": result_vulncount["Open Redirect"],
            "windows_directory_traversal": result_vulncount[
                "Windows Directory Traversal"
            ],
            "linux_directory_traversal": result_vulncount["Linux Directory Traversal"],
            "lfi": result_vulncount["LFI Check"],
            "rfi": result_vulncount["RFI Check"],
            "rce_linux": result_vulncount["RCE Linux Check"],
            "rce_php": result_vulncount["RCE PHP Check"],
            "ssti": result_vulncount["SSTI Check"],
        }

        targets_serializer = TargetsSerializer(data=target_data)

        try:
            if await sync_to_async(targets_serializer.is_valid)(raise_exception=True):
                await database_sync_to_async(targets_serializer.save)()
        except Exception as e:
            print(e)
            target_tuple = await database_sync_to_async(Targets.objects.get)(
                target=target
            )
            targets_serializer = TargetsSerializer(target_tuple, data=target_data)
            if await sync_to_async(targets_serializer.is_valid)(raise_exception=True):
                await database_sync_to_async(targets_serializer.save)()

            # {'target': [ErrorDetail(string='targets with this target already exists.', code='unique')]}
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
