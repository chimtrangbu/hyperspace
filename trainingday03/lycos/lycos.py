def generate_autocomplete(words):
    res = {}
    keys = []
    for x in words:
        for i in range(len(x)):
            if x[:i + 1] not in keys:
                keys.append(x[:i + 1])
    for x in keys:
        for y in words:
            if (y.startswith(x)):
                if x not in res.keys():
                    res[x] = {y}
                else:
                    res[x].add(y)
    return res
