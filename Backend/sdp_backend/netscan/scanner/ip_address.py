import os


def get_ip_address(url):
    # for windows
    # command = 'nslookup ' + url
    # for linux
    command = 'host ' + url
    process = os.popen(command)
    results = str(process.read())
    # for windows
    # marker = results.find('Address:') + 10
    # return results[marker:].splitlines()[3]
    # for linux
    marker = results.find('has address') + 12
    return results[marker:].splitlines()[0]

# print('ip_address.py : ' + get_ip_address('reddit.com'))
