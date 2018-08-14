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


def sadd(key, value):
    global r
    if not exists(key):
        r[key] = set([value])
    elif not isinstance(r[key], set):
        r[key] = set([value])
    else:
        r[key].add(value)


def smembers(key):
    return r[key] if (exists(key) and isinstance(r[key], set)) else None


def sunion(key1, key2):
    set1 = smembers(key1) if smembers(key1) is not None else set()
    set2 = smembers(key2)
    return set1.union(set2) if (set2 is not None) else set1


def sinter(key1, key2):
    set1 = smembers(key1) if smembers(key1) is not None else set()
    set2 = smembers(key2) if smembers(key2) is not None else set()
    return(set1 & set2)


def srem(key, value):
    global r
    if smembers(key) is not None and value in smembers(key):
        smembers(key).remove(value)
