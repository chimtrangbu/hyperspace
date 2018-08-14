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


def generate_table(s):
    if s.replace(' ', '') == '':
        return {}
    res = {}
    c_o = count_occurrences(s)
    s = s.split(' ')
    for c in c_o.keys():
        for w in c_o[c]:
            res[w] = {}
            for j in range(len(s)):
                if s[j] == w and j != len(s) - 1:
                    temp = res[w]
                    if s[j + 1] not in temp.keys():
                        temp[s[j + 1]] = int(1)
                    else:
                        temp[s[j + 1]] += 1
    return res
