def order_words(array):
    if array == []:
        return [[]]
    length = []
    res = []
    for x in array:
        if not(len(x) in length):
            length.append(len(x))
    length.sort()
    for x in length:
        group = []
        for y in array:
            if len(y) == x:
                group.append(y)
        group.sort()
        res.append(group)
    return res
