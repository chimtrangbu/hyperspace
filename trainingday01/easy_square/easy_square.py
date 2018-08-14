v = int(input())
c = input()
if (v == 1):
    print(c[0])
elif (v <= 0):
    print("Invalid value")
else:
    t = c[0]
    for x in range(v - 2):
        t += c[1]
    t += c[0]
    b = c[0]
    for x in range(v - 2):
        b += c[2]
    b += c[0]
    m = c[3]
    for x in range(v - 2):
        m += " "
    m += c[4]
    print(t)
    for x in range(v - 2):
        print(m)
    print(b)
