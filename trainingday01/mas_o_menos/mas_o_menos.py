res = int(input("What is the result? "))
print("OK, let's begin\n")
t = 10
while (t >= 0):
    if (t == 0):
        q = "Your guess? (Last guess) "
    elif (t == 5):
        q = "Your guess? (Half way done) "
    else:
        q = "Your guess? (" + str(t) + " left) "
    p = int(input(q))
    if (p == res):
        print("Congrats !")
        break
    elif (p < res):
        if ((res - p) > 50):
            print("It's way more")
        else:
            print("It's more")
    else:
        if ((p - res) > 50):
            print("It's way less")
        else:
            print("It's less")
    t -= 1
if (t < 0):
    print("You lose :(")
