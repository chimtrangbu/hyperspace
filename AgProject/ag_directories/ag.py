import os
import sys
import glob


def find_all(str, sub):
    result = []
    start = 0
    while True:
        start = str.find(sub, start)
        if start == -1:
            return result
        result.append(start)
        start += len(sub)


def find_key(file, key):
    result = ''
    if os.path.isfile(file):
        f = open(file, 'r')
        try:
            lines = f.readlines()
        except UnicodeDecodeError:
            lines = []
        f.close()
        for line in lines:
            if '--case-sensitive' in ops:
                if line[:-1].find(key) != -1:
                    number = str(lines.index(line) + 1)
                    number = '\033[1;33m' + number + '\033[0m:'
                    line = line.replace(key, ('\033[30;43m' + key + '\033[0m'))
                    result += (number + line)
            else:
                templine = line.lower()[:-1]
                key = sys.argv[1].lower()
                if templine.find(key) != -1:
                    linenumber = str(lines.index(line) + 1)
                    temp = '\033[1;33m' + linenumber + '\033[0m:'
                    index_of_keys = find_all(templine, key)
                    newline = line[:templine.find(key)]
                    for it in range(len(index_of_keys)):
                        i = index_of_keys[it]
                        j = i + len(key)
                        k = line[i:j]
                        newline += ('\033[30;43m' + k + '\033[0m')
                        if it + 1 == len(index_of_keys):
                            newline += line[j:]
                        else:
                            newline += line[j:index_of_keys[it + 1]]
                    temp += newline
                    result += temp
    if result == '':
        return None
    result = '\033[1;32m' + file + '\033[0m\n' + result
    return result


def is_hidden(path):
    p = path.split('/')
    for x in p:
        if x[0] == '.':
            return True
    return False


res = []
ops = []
for e in sys.argv:
    if e.startswith('--'):
        ops.append(e)
key = sys.argv[len(ops) + 1]
files = []
if len(sys.argv) == len(ops) + 2 or sys.argv[len(ops) + 2] == '.':
    # find the key in all files
    for x in os.walk('.'):
        for y in glob.glob(os.path.join(x[0], '*')):
            files.append(y[2:])
        for z in glob.glob(os.path.join(x[0], '.*')):
            files.append(z[2:])
    if '--hidden' not in ops:
        temp = []
        for file in files:
            if not is_hidden(file):
                temp.append(file)
        files = temp
    if files:
        files.sort()
        for file in files:
            if find_key(file, key) is not None:
                res.append(find_key(file, key))
elif os.path.isdir(sys.argv[len(ops) + 2]):
    path = sys.argv[len(ops) + 2]
    for x in os.walk(path):
        for y in glob.glob(os.path.join(x[0], '*')):
            files.append(y)
        for z in glob.glob(os.path.join(x[0], '.*')):
            files.append(z)
    if '--hidden' not in ops:
        temp = []
        for file in files:
            if not is_hidden(file):
                temp.append(file)
        files = temp
    if files:
        files.sort()
        for file in files:
            if find_key(file, key) is not None:
                res.append(find_key(file, key))
else:
    file = sys.argv[len(ops) + 2]
    output = find_key(file, key)
    if output:
        cut_output = output.split('\n')
        del cut_output[0]
        output = '\n'.join(cut_output)
        res.append(output)
print(end='\n'.join(res))
