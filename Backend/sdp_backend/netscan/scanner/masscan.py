import subprocess
import json

def get_masscan(port_range, ip_addresses, rate):
    cmd_reculsive = ['masscan', '-p' + port_range, ' '.join(ip_addresses), '--max-rate', rate]

    p = subprocess.Popen(cmd_reculsive,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,
                         universal_newlines=True)

    return p


# ip_addresses = ['223.130.195.95', '125.209.222.142', '223.130.195.200', '125.209.222.141']
# port_range = '80,443'
# rate = '100'
# filename = 'test'
# get_masscan(port_range, ip_addresses, rate, filename)
