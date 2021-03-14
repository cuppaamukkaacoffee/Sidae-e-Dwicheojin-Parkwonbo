import json as JSON
from channels.generic.websocket import WebsocketConsumer

from .scanner.domain_name import get_domain_name
from .scanner.ip_address import get_ip_address
from .scanner.nmap import get_nmap
from login.jwt import JwtHelper, AsyncJwtHelper
import channels.exceptions

from .serializers import (
    PortsSerializer,
    CrawledIPsSerializer,
)
import hashlib, datetime, random


class NetscanConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, message):
        self.send(text_data=JSON.dumps({"message": message}))
        self.close()

    def receive(self, text_data):
        random.seed(datetime.datetime.now())
        print(type(text_data))

        data_json = JSON.loads(text_data)
        jwt = JwtHelper()

        try:
            token = data_json["token"]
            target = data_json["target"]

            fast_scan = data_json["fast_scan"]

        except:
            print("nothing")
            self.disconnect(message="missing body attribute")
            raise channels.exceptions.StopConsumer

        verification = jwt.validate(token)
        print(verification)
        if not verification:
            self.disconnect(message="invalid token")
            raise channels.exceptions.StopConsumer
        elif type(verification) == str:
            self.disconnect(message=verification)
            raise channels.exceptions.StopConsumer

        scan_session_id = hashlib.md5(
            (str(random.random())).encode("utf-8")
        ).hexdigest()

        if target:
            self.send(text_data=JSON.dumps({"message": "collecting ip addresses..."}))
            if target[-1] != "/":
                target += "/"

            domain_name = get_domain_name(target)
            print(domain_name)
            ip_list = get_ip_address(domain_name)
            crawledIPs = []
            marker = ip_list.find('has address')
            while marker != -1:
                ip_address = ip_list[marker + 12:].splitlines()[0]
                self.send(text_data=JSON.dumps({"ip_address": ip_address}))
                crawledIPs.append(
                    {
                        "id": hashlib.md5(
                            (ip_address + verification.username).encode("utf-8")
                        ).hexdigest(),
                        "scan_session_id": scan_session_id,
                        "username": verification.username,
                        "target": target,
                        "ip_address": ip_address,
                    }
                )
                marker = ip_list.find('has address', marker + 13)

        ports = []
        if fast_scan:
            self.send(text_data=JSON.dumps({"message": "doing fast scan..."}))
            for ip_dict in crawledIPs:
                ip = ip_dict["ip_address"]
                print(ip)
                lines = get_nmap("-F -Pn", ip)
                for line in lines:
                    line_split = line.split()
                    port_number = line_split[0]
                    port_status = line_split[1]
                    port_service = line_split[2]

                    self.send(text_data=JSON.dumps({"ip_address": ip,
                                                    "port_number": port_number,
                                                    "port_status": port_status,
                                                    "port_service": port_service}))
                    ports.append(
                        {
                            "id": hashlib.md5(
                                (port_number + ip + verification.username).encode("utf-8")
                            ).hexdigest(),
                            "scan_session_id": scan_session_id,
                            "username": verification.username,
                            "target": target,
                            "ip_address": ip,
                            "port_number": port_number,
                            "port_status": port_status,
                            "port_service": port_service,
                        }
                    )
        ip_serializer = CrawledIPsSerializer(data=crawledIPs, many=True)
        port_serializer = PortsSerializer(data=ports, many=True)
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

        self.send(text_data=JSON.dumps({"status": "200"}))
        self.disconnect(message="all good")

        # else:
        #     await self.send(text_data=JSON.dumps({"message": "doing full scan..."}))
        #     for ip in ip_list:
        #         lines = get_nmap("-p1-65535 --open -Pn", ip)
        #         for line in lines:
        #             line_split = line.split()
        #             port_number = line_split[0]
        #             port_status = line_split[1]
        #             port_service = line_split[2]
        #
        #             ports.append(
        #                 {
        #                     "id": hashlib.md5(
        #                         (port_number + verification.username).encode("utf-8")
        #                     ).hexdigest(),
        #                     "fast_scan": False,
        #                     "scan_session_id": scan_session_id,
        #                     "username": verification.username,
        #                     "target": target,
        #                     "ip_address": ip,
        #                     "port_number": port_number,
        #                     "port_status": port_status,
        #                     "port_service": port_service,
        #                 }
        #             )
        #         lines = get_nmap("-p1-65535 -sU --open -Pn", ip)
        #         for line in lines:
        #             line_split = line.split()
        #             port_number = line_split[0]
        #             port_status = line_split[1]
        #             port_service = line_split[2]
        #
        #             ports.append(
        #                 {
        #                     "id": hashlib.md5(
        #                         (port_number + verification.username).encode("utf-8")
        #                     ).hexdigest(),
        #                     "fast_scan": False,
        #                     "scan_session_id": scan_session_id,
        #                     "username": verification.username,
        #                     "target": target,
        #                     "ip_address": ip,
        #                     "port_number": port_number,
        #                     "port_status": port_status,
        #                     "port_service": port_service,
        #                 }
        #             )