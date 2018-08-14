def print_tab(array):
    n = 0
    d = len(array) * 2
    max1 = 0
    for x in array:
        if len(x) > max1:
            max1 = len(x)
    max2 = 0
    for x in range(max1):
        for i in array:
            if len(i[x]) > max2:
                max2 = len(i[x])
        n += max2 + 3
    n += 1
    res = "+" * n + "\n"
    for x in range(d):
        if x % 2 == 1:
            res += ("+" * n + "\n")
        else:
            t = n
            for i in array[x // 2]:
                res += ("+ " + i + " ")
                t -=






  """Given one argument, this function returns nothing.

  >>> print_tab([["this"], ["~~", "is", "~~"], [ "ah!", "oh!", "kind", "", "eh !"], ["1", "2", "3", "of"], ["...", "...", "...", "...", "fun !"]])
  +++++++++++++++++++++++++++++++++++
  + this                            +
  +++++++++++++++++++++++++++++++++++
  + ~~   + is  + ~~                 +
  +++++++++++++++++++++++++++++++++++
  + ah!  + oh! + kind +     + eh !  +
  +++++++++++++++++++++++++++++++++++
  + 1    + 2   + 3    + of          +
  +++++++++++++++++++++++++++++++++++
  + ...  + ... + ...  + ... + fun ! +
  +++++++++++++++++++++++++++++++++++
  >>> print_tab([])
  ++
  ++
  >>> print_tab([[""]])
  ++++
  +  +
  ++++
  """
