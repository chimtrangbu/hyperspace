r = {}


def put(key, value):
    global r
    r[key] = value
    return value


def get(key):
    return r[key] if key in r.keys() else None


def exists(key):
    return (key in r.keys())


def delete(*keys):
    global r
    res = 0
    for k in keys:
        try:
            del r[k]
            res += 1
        except KeyError:
            pass
    return res


def incr(key):
    global r
    return incrby(key, 1)


def incrby(key, delta):
    global r
    if not exists(key):
        put(key, 0)
    elif not isinstance(r[key], (int, float)):
        raise ValueError('Incorrect value')
    r[key] += delta
    return r[key]


def sadd(key, *values):
    global r
    res = 0
    vals = set(values)
    if exists(key) and isinstance(r[key], set):
        for v in vals:
            if v not in r[key]:
                r[key].add(v)
                res += 1
        return res
    else:
        r[key] = vals
        return len(vals)


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


def srem(key, *values):
    global r
    res = 0
    values = set(values)
    if smembers(key) is not None:
        for value in values:
            if value in smembers(key):
                smembers(key).remove(value)
                res += 1
    return res
