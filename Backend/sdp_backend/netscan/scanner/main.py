from .domain_name import *
from .ip_address import *
from .nmap import *
from .robots import *
from .whois import *


def gather_info(name, url):
    domain_name = get_domain_name(url)
    print('domain_name : ' + domain_name)
    ip_address = get_ip_address(domain_name)
    print('ip_address : ' + ip_address)
    nmap = get_nmap('-F', ip_address)
    robots = get_robots_txt(url)
    whois = get_whois(domain_name)


gather_info('reddit', 'https://www.reddit.com/')
