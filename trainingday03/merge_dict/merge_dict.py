def merge_dict(dictionaries):
    res = {}
    keys = []
    for x in dictionaries:
        for y in x.keys():
            if y not in keys:
                keys.append(y)
    for d in dictionaries:
        for x in keys:
            if x in d.keys():
                if x not in res.keys():
                    res[x] = [d[x]]
                else:
                    res[x].append(d[x])
    return res
