import os


def get_nmap(options, ip):
    command = 'nmap ' + options + ' ' + ip
    process = os.popen(command)
    results = str(process.read())

    tmp = results.find("PORT")
    if tmp == -1:
        return []
    start = results.find("\n", tmp)
    end = results.find("\n\n", start)
    return results[start+1:end].splitlines()


# print(get_nmap('-F', '18.192.172.30'))
# print(get_nmap('-F --open -Pn', '18.192.172.30'))
# print(get_nmap('-p1-65535 --open -Pn', '18.192.172.30'))
# print(get_nmap('-p1-65535 -sU --open -Pn', '18.192.172.30'))
# ["nmap -p1-65535 --open -Pn ", ""],
# ["nmap -p1-65535 -sU --open -Pn ", ""],
# ["nmap -F --open -Pn ",""],