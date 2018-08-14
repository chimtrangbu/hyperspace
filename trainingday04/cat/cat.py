import os.path
import sys

if (len(sys.argv) >= 2):
    for filename in sys.argv[1:]:
        if os.path.isfile(filename):
            f = open(filename, 'r')
            lines = ''.join(f.readlines())
            f.close()
            print(end=lines)
else:
    s = ''.join(sys.stdin.readlines())
    print(end=s)
