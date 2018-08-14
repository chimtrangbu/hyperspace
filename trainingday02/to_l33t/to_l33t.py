def to_l33t(string):
    string = list(string)
    for x in range(len(string)):
        if string[x].lower() == 'a':
            string[x] = '4'
        elif string[x].lower() == 'e':
            string[x] = '3'
        elif string[x].lower() == 'i':
            string[x] = '1'
        elif string[x].lower() == 'o':
            string[x] = '0'
        elif string[x].lower() == 'u':
            string[x] = '8'
    res = ''.join(string)
    return res
