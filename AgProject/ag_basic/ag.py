import os.path
import sys


def find_all(str, sub):
    result = []
    start = 0
    while True:
        start = str.find(sub, start)
        if start == -1:
            return result
        result.append(start)
        start += len(sub)


# sys.argv = ["--case-sensitive", "hello", "file1", "file2
res = []
if sys.argv[1] == "--case-sensitive":
    key = sys.argv[2]
    if os.path.isfile(sys.argv[3]):
        f = open(sys.argv[3], 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
            key = sys.argv[2]
            if line[:-1].find(key) != -1:
                linenumber = str(lines.index(line) + 1)
                temp = '\033[1;33m' + linenumber + '\033[0m:'
                line = line.replace(key, ('\033[30;43m' + key + '\033[0m'))
                temp += line
                res.append(temp)
# elif len(sys.argv) == 2:  # find key in all files
#     key = sys.argv[1].lower()
else:
    key = sys.argv[1].lower()
    if os.path.isfile(sys.argv[2]):
        f = open(sys.argv[2], 'r')
        lines = f.readlines()
        f.close()
        for line in lines:
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
                res.append(temp)
print(end=''.join(res))
