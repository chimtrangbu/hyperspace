def check(player):
    allow = ("rock", "paper", "scissors")
    for i in allow:
        if (i == player):
            return True
    return False


p1 = input("Player 1? ")
p2 = input("Player 2? ")
if not(check(p1) and check(p2)):
    print("Error.")
elif (p1 == p2):
    print("Draw.")
elif (p1 == "rock"):
    if (p2 == "paper"):
        print("Player 2 wins.")
    else:
        print("Player 1 wins.")
elif (p1 == "paper"):
    if (p2 == "rock"):
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
else:
    if (p2 == "rock"):
        print("Player 2 wins.")
    else:
        print("Player 1 wins.")
