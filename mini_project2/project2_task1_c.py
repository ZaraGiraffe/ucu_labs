from argparse import ArgumentParser as Arg
import os

def code(char, off):
    b = char == char.lower()
    a = 'a'
    z = 'z'
    if ord(char) >= ord('а') and ord(char) <= ord('я'):
        a = 'а'
        z = 'я'
    if off < 0:
        off += ord(z) - ord(a) + 1
    neword = ord(char) + off
    if neword > ord(z):
        neword = ord(a) + neword - ord(z) - 1
    if b:
        return chr(neword)
    else:
        return chr(neword).upper()


par = Arg(description='Ceasers code')
par.add_argument('path', help='path to the document')
par.add_argument('--offset', default=13, type=int, help='how to code the file')
par.add_argument('--inplace', help='how to change the file', nargs='*')
par.add_argument('--decrypt', help='if you want to decrypt the file', nargs='*')


if __name__ == '__main__':
    obj = par.parse_args()
    if not os.path.exists(obj.path):
        print("there is no such file")
        exit()
    newfile = []
    off = obj.offset if obj.decrypt == None else -obj.offset
    with open(obj.path, 'r') as file:
        for line in file:
            lst = []
            for i in line:
                lst.append(i)
            for i, ch in enumerate(lst):
                if ch.isalpha():
                    lst[i] = code(ch, off)
            newfile.append(''.join(lst))
    if obj.inplace == None:
        for i in newfile:
            print(i, end='')
    else:
        with open(obj.path, 'w') as file:
            for i in newfile:
                file.write(i)
