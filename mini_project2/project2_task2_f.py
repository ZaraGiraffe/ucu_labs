import re, argparse, os

par = argparse.ArgumentParser(description='finds substring in file')
par.add_argument('path', help='path to directory')
par.add_argument('regularka', help='regular expression')
par.add_argument('--showlines', help='shows all line', nargs='*')
par.add_argument('--only_show_counts', help='counts the number of substrings', nargs='*')


if __name__ == '__main__':
    obj = par.parse_args()
    if not os.path.exists(obj.path):
        print('there is no such directory')
        exit()
    res = []
    with open(obj.path, 'r') as file:
        for i, v in enumerate(file.readlines()):
            if re.search(obj.regularka, v.strip('\n')):
                res.append((i+1, v.strip('\n')))
    if obj.showlines != None:
        for i in res:
            print(f'{i[0]:}', i[1])
        exit()
    if obj.only_show_counts != None:
        print(len(res))
        exit()
    for i in res:
        print(i[1])
