def itranslate(dic, string):
    s = string.split(' ')
    for i in range(len(s)):
        if s[i] not in dic.keys():
            raise KeyError('Missing word')
        else:
            s[i] = dic[s[i]]
    res = ' '.join(s)
    return res
