n = int(input("What is the size of your train? "))
if (n == 1):
    print(" ______________________>__")
    print("|]||[]_[]_[]|||[]_[]_[]||[|")
    print("\\==o-o======o-o======o-o==/")
elif (n > 1):
    head1 = " ______________________>__"
    line1 = " _________________________  " * (n - 1) + head1
    head2 = "|]||[]_[]_[]|||[]_[]_[]||[|"
    line2 = "|]||[]_[]_[]|||[]_[]_[]||[| " * (n - 1) + head2
    head3 = "\\==o-o======o-o======o-o==/"
    line3 = "\\==o-o======o-o======o-o==/_" * (n - 1) + head3
    print(line1)
    print(line2)
    print(line3)
elif (n < 0):
    print("Don't be so negative.")
