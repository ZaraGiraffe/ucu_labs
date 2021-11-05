import zipfile, argparse, os, re


par = argparse.ArgumentParser(description='finds all files with the substring and add them to new.zip')
par.add_argument('regularka', help='regular expression')
par.add_argument('path', help='path to directory')
par.add_argument('dst', help='where to save the files')


if __name__ == '__main__':
    obj = par.parse_args()
    if not os.path.exists(obj.path) or not os.path.exists(obj.dst):
        print('there is no such directory')
        exit()
    
    with zipfile.ZipFile(os.path.join(obj.dst, 'new.zip'), 'w') as wr:
        os.mkdir(os.path.join(obj.dst, 'add'))
        z = zipfile.ZipFile(obj.path, 'r')
        z.extractall(path=os.path.join(obj.dst, 'add'))
        for root, dirs, files in os.walk(os.path.join(obj.dst, 'add')):
            for file in files:
                with open(os.path.join(root, file)) as f:
                    s = f.read()
                    if re.search(obj.regularka, s):
                        newfile = open(os.path.join(obj.dst, file), 'w')
                        newfile.write(s)
                        newfile.close()
                        wr.write(os.path.join(obj.dst, file))
                        os.remove(os.path.join(obj.dst, file))
        for root, dirs, files in os.walk(os.path.join(obj.dst, 'add'), topdown=False):
            for i in files:
                os.remove(os.path.join(root, i))
            for j in dirs:
                os.rmdir(os.path.join(root, j))
        os.rmdir(os.path.join(obj.dst, 'add'))
