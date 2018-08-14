r = {}


def put(key, value):
    global r
    r[key] = value


def get(key):
    return r[key] if key in r.keys() else None
