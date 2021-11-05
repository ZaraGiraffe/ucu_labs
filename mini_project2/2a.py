'''
./
├── dir2/
│  ├── file2
│  └── file3
└── file1
'''
import argparse, os
from posixpath import dirname

par = argparse.ArgumentParser(description='make a tree')
par.add_argument('path', help='path to directory')


cons = ['├──', '│  ', '└──', '   ']
def recursion(path):
    if not os.path.isdir(path):
        return [os.path.basename(path)]
    name = os.path.basename(path) + '/'
    res = [name]
    for i, dir in enumerate(os.listdir(path)):
        if i == len(os.listdir(path)) - 1:
            for j, line in enumerate(recursion(os.path.join(path, dir))):
                if j == 0:
                    res.append(cons[2] + line)
                else:
                    res.append(cons[3] + line)
        else:
            for j, line in enumerate(recursion(os.path.join(path, dir))):
                if j == 0:
                    res.append(cons[0] + line)
                else:
                    res.append(cons[1] + line)
    return res


if __name__ == '__main__':
    obj = par.parse_args()
    if not os.path.exists(obj.path):
        print('there is no such directory')
        exit()
    res = recursion(obj.path)
    for i in res:
        print(i)

