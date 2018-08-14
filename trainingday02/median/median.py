n = input("Give me a series of numbers and I will give you their median.\n")
ar = []
c = 0
while (n):
    ar.append(int(n))
    c += 1
    n = input()
ar.sort()
if c == 0:
    print("Error, empty dataset")
elif c % 2 == 1:
    res = ar[c // 2]
    print("The median is", res)
else:
    res = (ar[c // 2 - 1] + ar[c // 2]) / 2
    print("The median is", res)
