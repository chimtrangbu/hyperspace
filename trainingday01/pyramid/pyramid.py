s = int(input("What pyramid size do you want?\n"))
h = int(((s + 1) / 2))
for x in range(h):
    m = ' ' * (h - 1 - x)
    t = '#' * (2 * x + 1)
    m += t
    print(m)
