import os, argparse

par = argparse.ArgumentParser(description='copy directory')
par.add_argument('src', help='source')
par.add_argument('dst', help='destination')


def make_lst(src):
    if os.path.isfile(src):
        res = b''
        with open(src, 'rb') as file:
            res = file.read()
        return (os.path.basename(src), res)
    res = []
    for file in os.listdir(src):
        res.append(make_lst(os.path.join(src, file)))
    return (os.path.basename(src), res)


def print_lst(lst, dst):
    dst = os.path.join(dst, lst[0])
    if not isinstance(lst[1], list):
        with open(dst, 'wb') as file:
            file.write(lst[1])
            return
    if not os.path.exists(dst):
        os.mkdir(dst)
    for i in lst[1]:
        print_lst(i, dst)


if __name__ == '__main__':
    obj = par.parse_args()
    if not os.path.exists(obj.src) or not os.path.exists(obj.dst):
        print('wrong paths')
        exit()
    lst = make_lst(obj.src)
    print_lst(lst, obj.dst)

