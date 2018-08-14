money = int(input("What's the bill ? "))
if money == 0:
    print("Oh, it was free !")
elif money < 0:
    print("Well, it's you who owes me money then.")
else:
    value = (10000, 5000, 2000, 1000, 500, 100, 50, 10, 5, 1)
    for x in range(10):
        f = money // value[x]
        money %= value[x]
        if f > 0:
            if value[x] >= 1000:
                print(f, value[x], "banknote")
            else:
                print(f, value[x], "coin")
