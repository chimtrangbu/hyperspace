c = 0
v = int(input("Value? "))
while (c < v):
    c += 1
    if (c % 5 != 0 and c % 9 != 0):
        print(c)
    elif (c % 5 == 0 and c % 9 == 0):
        print('InTek')
    elif (c % 5 == 0):
        print("In")
    else:
        print("Tek")
