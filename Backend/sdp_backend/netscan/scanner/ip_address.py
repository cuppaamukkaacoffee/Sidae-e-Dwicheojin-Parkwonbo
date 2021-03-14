import os


def get_ip_address(url):
    command = 'host ' + url
    process = os.popen(command)
    results = str(process.read())

    return results

# print(get_ip_address('naver.com'))
