import time

r = {}


def put(key, value, expires_in=60):
    r[key] = {"value": value, "time": time.time() + expires_in}
    return value


def get(key):
    return r[key]["value"] if
    (key in r.keys() and r[key]["time"] <= time.time()) else None
#done

def exists(key):
    if (key in r.keys()):
        return (r[key]["time"] <= time.time())
    return False

def delete(*keys):
    res = 0
    for k in keys:
        if exists(key):
            del r[key]
            res += 1
    return res
#done

def incr(key):
    return incrby(key, 1)


def incrby(key, delta):
    if not exists(key):
        put(key, 0)
    elif not isinstance(r[key]["value"], (int, float)):
        raise ValueError('Incorrect value')
    r[key]["value"] += delta
    return r[key]["value"]
#done

def sadd(key, *values, expires_in=None):
    if expires_in == None:
        res = 0
        vals = set(values)
        if exists(key) and isinstance(r[key]["value"], set):
            for v in vals:
                if v not in r[key]["value"]:
                    r[key]["value"].add(v)
                    res += 1
            return res
        else:
            r[key]["value"] = vals
            return len(vals)
    else:
        tempvals = set(values)
        if exists(key) and isinstance(r[key]["value"], set):
            r[key]["tempvalue"] = tempvals | r[key]["value"]
            r[key]["time"] = time.time() + expires_in
            return len(r[key]["tempvalue"])
        else:
            r[key]["tempvalue"] = vals
            r[key]["time"] = time.time() + expires_in
            return len(tempvals)
#done

def smembers(key):
    if exists(key) and isinstance(r[key]["value"], set):
        if "time" in r[key].keys() and r[key]["time"] <= time.time():
            return r[key]["value"] | r[key]["tempvalue"]
        return r[key]["value"]
    return None


def sunion(key1, key2):
    set1 = smembers(key1) if smembers(key1) is not None else set()
    set2 = smembers(key2)
    return set1.union(set2) if (set2 is not None) else set1


def sinter(key1, key2):
    set1 = smembers(key1) if smembers(key1) is not None else set()
    set2 = smembers(key2) if smembers(key2) is not None else set()
    return(set1 & set2)
#done

def srem(key, *values):
    res = 0
    values = set(values)
    if smembers(key) is not None:
        for value in values:
            if value in smembers(key):
                smembers(key).remove(value)
                res += 1
    return res


def hset(key, hash_key, hash_value, expires_in=None):
    if expires_in == None:
        try:
            dok = r[key]["value"]
            if isinstance(r[key]["value"], dict):
                dok[hash_key] = hash_value
            else:
                dok = {hash_key: hash_value}
            r[key]["value"] = dok
        except not exists(key):
            r[key] = {"value": {hash_key: hash_value}}
        return {hash_key: hash_value}
    else:
        if exists(key):
            ####################
        else:
            r[key] = {"value": {hash_key: hash_value},
            "time": time.time() + expires_in}



def hget(key, hash_key):
    if exists(key) and isinstance(r[key]["value"], dict):
        hash_key in r[key]["value"]:
        return r[key][hash_key]
    else:
        return None


def hgetall(key):
    try:
        return r[key]
    except KeyError:
        return None


print(time.time())
