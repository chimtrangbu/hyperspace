def html_parser(html):
    if "<" not in html:
        return html
    list = html.split("<")
    if list[0] == '':
        list = list[1:]
    rem = []
    for x in list:
        if (x[-1] == ">"):
            rem.append(x)
    for x in rem:
        for y in list:
            if y == x:
                list.remove(y)
    res = []
    for x in list:
        for i in range(len(x)):
            if x[i] == ">":
                res.append(x[i + 1:])
                break
    res = ''.join(res)
    return res

print(html_parser("hkfbkrchfnrle"))
