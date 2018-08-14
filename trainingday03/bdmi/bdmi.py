def bdmi(dic):
    res = {}
    movies = []
    for x in dic.keys():
        movies.append(x)
    actors = []
    for x in movies:
        for y in dic[x]:
            if y not in actors:
                actors.append(y)
    for x in actors:
        for y in movies:
            if x in dic[y]:
                if x not in res.keys():
                    res[x] = [y]
                else:
                    res[x].append(y)
    return res
