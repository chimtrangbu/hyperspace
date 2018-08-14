def rotx(s, x=13):
    x = x % 26
    dic = {}
    res = []
    for i in range(97, 123 - x):
        dic[chr(i)] = chr(i + x)
    for i in range(123 - x, 123):
        dic[chr(i)] = chr(i + x - 26)
    for i in range(65, 91 - x):
        dic[chr(i)] = chr(i + x)
    for i in range(91 - x, 91):
        dic[chr(i)] = chr(i + x - 26)
    for q in s:
        if q in dic.keys():
            res.append(dic[q])
        else:
            res.append(q)
    return ''.join(res)
