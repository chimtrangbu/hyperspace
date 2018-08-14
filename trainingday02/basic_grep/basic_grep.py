def basic_grep(text, string):
    res = []
    lines = text.split("\n")
    if string[0] == '^' and string[-1] == '$':
        for x in lines:
            if x == string[1:-1]:
                res.append(x)
    elif string[0] == '^':
        for x in lines:
            if x[:len(string)] == string[1:]:
                res.append(x)
    elif string[-1] == '$':
        for x in lines:
            i = -len(string) + 1
            if x[i:] == string[:-1]:
                res.append(x)
    else:
        for x in lines:
            if x.find(string) != -1:
                res.append(x)
    return res
