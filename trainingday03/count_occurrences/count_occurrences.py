def count_occurrences(string):
    res = {}
    string = string.split(' ')
    temp = []
    for x in string:
        if x not in temp:
            temp.append(x)
    for x in temp:
        c = 0
        for y in string:
            if y == x:
                c += 1
        if c not in res.keys():
            res[c] = [x]
        else:
            res[c].append(x)
    for x in res.keys():
        res[x].sort()
    return res
