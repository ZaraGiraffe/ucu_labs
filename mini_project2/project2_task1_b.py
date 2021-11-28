from argparse import ArgumentParser as Arg
import os


par = Arg(description="change file")
par.add_argument('fro', help='changed substring')
par.add_argument('to', help='to what program will change')
par.add_argument('path', help='path to the document')
par.add_argument('--inplace', help='how to change the file', nargs='*')


if __name__ == '__main__':
    obj = par.parse_args()
    newfile = []
    if os.path.exists(obj.path):
        with open(obj.path, 'r') as file:
            for line in file:
                newfile.append(line.replace(obj.fro, obj.to))
        if obj.inplace != None:
            with open(obj.path, 'w') as file:
                for line in newfile:
                    file.write(line)
        else:
            for line in newfile:
                print(line, end='')
    else:
        print('the file does not exist')
