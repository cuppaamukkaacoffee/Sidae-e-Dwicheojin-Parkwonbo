import json as JSON
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer

from .scanner.domain_name import get_domain_name
from .scanner.ip_address import get_ip_address
from .scanner.nmap import get_nmap
from .scanner.masscan import get_masscan
from .scanner.py_whois import get_whois
from login.jwt import JwtHelper, AsyncJwtHelper
import channels.exceptions

from .serializers import (
    PortsSerializer,
    CrawledIPsSerializer,
    TargetsSerializer,
    WhoissSerializer
)
import hashlib, datetime, random
import asyncio


class NetscanConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, message):
        self.send(text_data=JSON.dumps({"message": message}))
        self.close()
        raise channels.exceptions.StopConsumer

    def receive(self, text_data):
        random.seed(datetime.datetime.now())
        print(type(text_data))

        data_json = JSON.loads(text_data)
        jwt = JwtHelper()

        try:
            token = data_json["token"]
            target = data_json["target"]
            port_range = data_json["port_range"]
            rate = data_json["rate"]
            whois_flag = data_json["whois_flag"]
        except:
            print("nothing")
            self.disconnect(message="missing body attribute")

        verification = jwt.validate(token)
        print(verification)
        if not verification:
            self.disconnect(message="invalid token")
        elif type(verification) == str:
            self.disconnect(message=verification)

        scan_session_id = hashlib.md5(
            (str(random.random())).encode("utf-8")
        ).hexdigest()

        if target:
            if target[-1] != "/":
                target += "/"
            if whois_flag:
                self.send(text_data=JSON.dumps({"message": "collecting whois information..."}))
                w = get_whois(target)
                w = {key: value for key, value in w.items() if key in [
                    'domain_name', 'registrar', 'whois_server', 'referral_url', 'updated_date',
                    'creation_date', 'expiration_date', 'name_servers', 'status', 'emails', 'dnssec', 'name',
                    'org', 'address', 'city', 'state', 'zipcode', 'country']}
                w['id'] = hashlib.md5(
                    (scan_session_id + verification.username).encode("utf-8")
                ).hexdigest()
                w['scan_session_id'] = scan_session_id
                w['username'] = verification.username
                w['target'] = target
                self.send(JSON.dumps({'whois': w}))

                whois_serializer = WhoissSerializer(data=w)
                try:
                    if whois_serializer.is_valid():
                        whois_serializer.save()
                    else:
                        print(whois_serializer.errors)
                except Exception as e:
                    print(e)
            self.send(text_data=JSON.dumps({"message": "collecting ip addresses..."}))
            domain_name = get_domain_name(target)
            print(domain_name)
            ip_plus_dummy = get_ip_address(domain_name)
            crawledIPs = []
            ip_list = []

            marker = ip_plus_dummy.find('has address')
            while marker != -1:
                ip_address = ip_plus_dummy[marker + 12:].splitlines()[0]
                self.send(text_data=JSON.dumps({"collected_ip": ip_address}))

                ip_list.append(ip_address)
                crawledIPs.append(
                    {
                        "id": hashlib.md5(
                            (ip_address + scan_session_id + verification.username).encode("utf-8")
                        ).hexdigest(),
                        "scan_session_id": scan_session_id,
                        "username": verification.username,
                        "target": target,
                        "ip_address": ip_address,
                    }
                )
                marker = ip_plus_dummy.find('has address', marker + 13)

        else:
            self.disconnect(message="invalid target")
            raise channels.exceptions.StopConsumer

        self.send(text_data=JSON.dumps({"message": "scanning for open ports..."}))
        open_ports = 0

        ports = []
        if not port_range:
            port_range = "0-65535"
        if not rate:
            rate = "5000"
        p = get_masscan(port_range, ip_list, rate)
        process_number = "0"
        while p.poll() == None:
            out = p.stdout.readline()
            if out.startswith('Discovered open port'):
                start = out.find('port ')
                mid = out.find('/', start)
                end = out.find(' ', mid)
                port_number = out[start + 5:mid]
                port_protocol = out[mid + 1:end]

                start = out.find('on ')
                end = out.find('\n', start)
                ip_address = out[start + 3:end].rstrip(" ")

                open_port = {
                    "id": hashlib.md5(
                        (port_number + ip_address + verification.username).encode("utf-8")
                    ).hexdigest(),
                    "scan_session_id": scan_session_id,
                    "username": verification.username,
                    "target": target,
                    "ip_address": ip_address,
                    "port_number": port_number,
                    "port_protocol": port_protocol,
                    "port_status": "open"
                }

                self.send(JSON.dumps(open_port))
                ports.append(open_port)

                open_ports = open_ports + 1
            elif out.startswith('rate: '):
                start = out.find('rate: ')
                end = out.find(',', start)
                rate = out[start + 6:end]

                start = end + 1
                end = out.find(' done', start)
                process = out[start:end].lstrip(" ")

                if int(float(process[:-1])) % 10 != process_number and \
                        float(process[:-1]) != 100.0:
                    self.send(JSON.dumps({'rate': rate, 'process': process}))
                    process_number = str((int(process_number) + 1) % 10)

        # self.send(JSON.dumps({'port list': ports}))

        ip_serializer = CrawledIPsSerializer(data=crawledIPs, many=True)
        port_serializer = PortsSerializer(data=ports, many=True)
        target_serializer = TargetsSerializer(data={"id": scan_session_id, "target": target,
                                                    "username": verification.username,
                                                    "scan_session_id": scan_session_id,
                                                    "open_ports": open_ports})
        try:
            if ip_serializer.is_valid():
                ip_serializer.save()
        except Exception as e:
            print(e)
        try:
            if port_serializer.is_valid():
                port_serializer.save()
        except Exception as e:
            print(e)
        try:
            if target_serializer.is_valid():
                target_serializer.save()
        except Exception as e:
            print(e)

        self.send(text_data=JSON.dumps({"status": "200"}))
        self.disconnect(message="all good")
