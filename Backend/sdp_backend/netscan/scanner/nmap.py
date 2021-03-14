import os


def get_nmap(options, ip):
    command = 'nmap ' + options + ' ' + ip
    process = os.popen(command)
    results = str(process.read())
    return results


# print('nmap.py : ' + get_nmap('-F', '104.25.98.99'))
