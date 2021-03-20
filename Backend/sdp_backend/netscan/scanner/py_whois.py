import whois

def timeobj_to_str(obj):
    new_obj_list = []
    if type(obj) == list:
        for item in obj:
            new_obj_list.append(item.strftime("%Y-%m-%d %H:%M:%S.%f"))
        return new_obj_list
    else:
        return obj.strftime("%Y-%m-%d %H:%M:%S.%f")

def to_list(w):
    for key, value in w.items():
        if type(value) == str:
            w[key] = [value]
        elif value is None:
            w[key] = [""]
    return w

def get_whois(target):
    w = whois.whois(target)

    w['updated_date'] = timeobj_to_str(w['updated_date'])
    w['creation_date'] = timeobj_to_str(w['creation_date'])
    w['expiration_date'] = timeobj_to_str(w['expiration_date'])

    w = to_list(w)
    return w
