r = {}


def put(key, value):
    global r
    r[key] = value


def get(key):
    return r[key] if key in r.keys() else None


def exists(key):
    return (key in r.keys())


def delete(key):
    global r
    try:
        del r[key]
    except KeyError:
        pass


def incr(key):
    global r
    incrby(key, 1)


def incrby(key, delta):
    global r
    if not exists(key):
        put(key, 0)
    elif not isinstance(r[key], (int, float)):
        raise ValueError('Incorrect value')
    r[key] += delta
