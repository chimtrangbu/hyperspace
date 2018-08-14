import os.path


def french_rap(csv):
    if not os.path.isfile(csv):
        raise FileNotFoundError('File does not exist')
    else:
        res = {}
        file = open(csv, 'r')
        lines = file.readlines()
        file.close()
        for i in range(len(lines)):
            temp = lines[i].replace('\n', '')
            lines[i] = temp.split(',')
        for x in lines:
            if x[1] not in res.keys():
                res[x[1]] = [x[0]]
            else:
                res[x[1]].append(x[0])
        return res
