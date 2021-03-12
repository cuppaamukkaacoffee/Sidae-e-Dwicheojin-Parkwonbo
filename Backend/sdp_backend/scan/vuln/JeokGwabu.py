import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse, quote_plus
from pprint import pprint
import asyncio
import random, hashlib
from datetime import datetime
import json
from aiohttp import ClientSession

# s = requests.Session()
# s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"


async def get_all_forms(session, url):
    """Given a `url`, it returns all forms from the HTML content"""
    res = await session.get(url)
    soup = bs(await res.read(), "html.parser")
    return soup.find_all("form")


def get_form_details(form):
    """
    This function extracts all possible useful information about an HTML `form`
    """
    details = {}

    try:
        action = form.attrs.get("action").lower()
    except:
        action = None

    method = form.attrs.get("method", "get").lower()

    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})

    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


def is_vulnerable(response):
    """A simple boolean function that determines whether a page
    is SQL Injection vulnerable from its `response`"""
    errors = {
        "you have an error in your sql syntax;",
        "warning: mysql",
        "unclosed quotation mark after the character string",
        "quoted string not properly terminated",
    }

    for error in errors:
        if error in response:
            return True

    return False


async def scan_sql_injection(
    session, url, target, sub_path, scan_session_id, username, vulncount
):

    reports = []
    requests = []
    responses = []
    # for c in "\"'":

    #     new_url = f"{url}{c}"
    #     print("[!] Trying", new_url)

    #     res = s.get(new_url)
    #     if is_vulnerable(res):

    #         print("[+] SQL Injection vulnerability detected, link:", new_url)
    #         return
    count = 0
    forms = await get_all_forms(session, url)
    # print(f"[+] Detected {len(forms)} forms on {url}.")
    for form in forms:
        result_string = "benign"
        form_details = get_form_details(form)
        for c in ['"', "'"]:

            data = {}
            for input_tag in form_details["inputs"]:
                if input_tag["type"] == "hidden" or input_tag["value"]:

                    try:
                        data[input_tag["name"]] = input_tag["value"] + c
                    except:
                        pass
                elif input_tag["type"] != "submit":

                    data[input_tag["name"]] = f"test{c}"

            url = urljoin(url, form_details["action"])
            if form_details["method"] == "post":
                res = await session.post(url, data=data)
            elif form_details["method"] == "get":
                res = await session.get(url, params=data)

            http_response = (await res.read()).decode("utf-8")
            http_length = len(http_response)
            http_status = res.status

            if is_vulnerable(http_response):
                result_string = "vulnerable"
                vulncount["SQL Injection"] += 1

            now = datetime.now()
            current_time = now.strftime("%Y-%m-%dT%H:%M")

            id = hashlib.md5((url + str(random.random())).encode("utf-8")).hexdigest()

            report = {
                "id": id,
                "scan_session_id": scan_session_id,
                "scan_type": "form_fuzz",
                "timestamp": current_time,
                "username": username,
                "target": target,
                "sub_path": sub_path,
                "vulnerability": "SQL Injection",
                "status": http_status,
                "url": url,
                "result_string": result_string,
                "form": str(form),
            }
            request = {
                "id": id,
                "host": target,
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "User-Agent": "Python/3.9 aiohttp/3.7.3",
                "body": json.dumps(dict(data)),
            }
            response = {
                "id": id,
                "headers_string": json.dumps(dict(res.headers)),
            }

            reports.append(report)
            requests.append(request)
            responses.append(response)

    return reports, requests, responses
    # print("[+] SQL Injection vulnerability detected, link:", url)
    # print("[+] Form:")
    # pprint(form_details)
    # return True
    # break


async def submit_form(session, form_details, url, value):

    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}

    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")

        if input_name and input_value:
            data[input_name] = input_value
    # print(data)
    if form_details["method"] == "post":
        return await session.post(target_url, data=data), data
    else:
        return await session.get(target_url, params=data), data


async def scan_xss(
    session, url, target, sub_path, scan_session_id, username, vulncount
):

    reports = []
    requests = []
    responses = []
    count = 0
    forms = await get_all_forms(session, url)
    js_script = "<Script>alert('hi')</scripT>"
    payload = quote_plus("<Script>alert('hi')</scripT>")
    payloads = [js_script, payload]

    if forms == []:
        print(f"form: {forms}")
        return reports, requests, responses

    for form in forms:
        # print(str(form))
        for payload in payloads:
            result_string = "benign"
            form_details = get_form_details(form)
            res, body = await submit_form(session, form_details, url, payload)
            http_response = (await res.read()).decode("utf-8")
            http_length = len(http_response)
            http_status = res.status

            if js_script in http_response:
                result_string = "vulnerable"
                vulncount["XSS"] += 1

            now = datetime.now()
            current_time = now.strftime("%Y-%m-%dT%H:%M")

            id = hashlib.md5((url + str(random.random())).encode("utf-8")).hexdigest()

            report = {
                "id": id,
                "scan_session_id": scan_session_id,
                "scan_type": "form_fuzz",
                "timestamp": current_time,
                "username": username,
                "target": target,
                "sub_path": sub_path,
                "vulnerability": "XSS",
                "status": http_status,
                "url": url,
                "result_string": result_string,
                "form": str(form),
            }
            request = {
                "id": id,
                "host": target,
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate",
                "User-Agent": "Python/3.9 aiohttp/3.7.3",
                "body": json.dumps(body),
            }
            response = {
                "id": id,
                "headers_string": json.dumps(dict(res.headers)),
            }

            reports.append(report)
            requests.append(request)
            responses.append(response)
            # print(f"[+] Detected {len(forms)} forms on {url}.")
            # print(f"[+] XSS Detected on {url}")
            # print(f"[*] Form details:")
            # pprint(form_details)
            # is_vulnerable = True

    return reports, requests, responses


async def main(session, username, url, scan_session_id):
    reports_list = []
    requests_list = []
    responses_list = []
    count = 0
    vulncount = {"SQL Injection": 0, "XSS": 0}
    parsed = urlparse(url)
    random.seed(int(datetime.now().timestamp()))
    target = "{uri.scheme}://{uri.netloc}".format(uri=parsed)
    sub_path = url.split(target)[1]

    reports, requests, responses = await scan_sql_injection(
        session, url, target, sub_path, scan_session_id, username, vulncount
    )

    reports_list += reports
    requests_list += requests
    responses_list += responses

    reports, requests, responses = await scan_xss(
        session, url, target, sub_path, scan_session_id, username, vulncount
    )

    reports_list += reports
    requests_list += requests
    responses_list += responses

    if reports_list == [] or requests_list == [] or responses_list == []:
        print(f"empty string at {url} due to zero forms")

    await session.close()
    return reports_list, requests_list, responses_list, vulncount


async def testMain():

    session = ClientSession()
    url = "http://testphp.vulnweb.com/artists.php?artist=1"
    url2 = "http://testphp.vulnweb.com/userinfo.php"

    await main(session, "aaa", url2, "test")


# asyncio.run(testMain())
