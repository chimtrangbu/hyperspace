def concat_files(*elements):
    f = open("concatenated_files", "w+")
    for x in elements:
        file = open(x, 'r')
        lines = file.readlines()
        file.close()
        for y in lines:
            f.write(y)
    f.close()
