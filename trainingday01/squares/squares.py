n = int(input("How many squares do you need?\n"))
c = 4 * n - 1
for x in range(c // 2):
    if x % 2 == 0:
        t = ['#'] * c
        i = 1
        while i <= x:
            t[i] = ' '
            t[-i - 1] = ' '
            i += 2
        print(''.join(t))
    else:
        t = [' '] * c
        i = 0
        while i <= x:
            t[i] = '#'
            t[-i - 1] = '#'
            i += 2
        print(''.join(t))
x = c // 2
while x >= 0:
    if x % 2 == 0:
        t = ['#'] * c
        i = 1
        while i <= x:
            t[i] = ' '
            t[-i - 1] = ' '
            i += 2
        print(''.join(t))
    else:
        t = [' '] * c
        i = 0
        while i <= x:
            t[i] = '#'
            t[-i - 1] = '#'
            i += 2
        print(''.join(t))
    x -= 1
