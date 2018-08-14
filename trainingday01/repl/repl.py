def check1(f):
    b = ('a', 'e', 'u', 'i', 'o')
    if f not in b:
        return False
    return True


def check2(t):
    c = ("ls", "cat", "rev", "pwd")
    if t not in c:
        return False
    return True


s = 'string'
while (s):
    s = input("repl> ")
    if (s == 'quit'):
        break
    if (len(s) == 6):
        print("My length is 6")
    if (check1(s[0])):
        o = s[1] + s[2] + s[3]
        for i in range(4):
            print(o)
    if (check2(s)):
        print("I know the command", s, "!!")
    if ((s[0] == '0') and (s[-1] != '9')):
        for j in range(len(s)):
            if (s[j].isdigit()):
                print(s[j])
