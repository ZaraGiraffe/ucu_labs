from typing import List
import urllib.request as ur

def read_input_file(url: str, number: int) -> List[List[str]]:
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77

    Return list of strings lists from url

    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    if number == 0:
        return []
    file = ur.urlopen(url)
    count = 1
    res = []
    newl = []
    for line in file:
        if count <= 2:
            count += 1
            continue
        stri = line.decode('utf-8').strip().split()
        if stri[0] in ['Математика', 'Фізика', 'Іноземна', 'Переможець', 'РK:', 'CK:', '—', 'Олімпіада']:
            continue
        if stri[0] == 'Середній':
            newl.append(stri[5])
            res.append(newl)
            newl = []
            if len(res) == number:
                break
            continue
        newl += [stri[0], stri[1] + ' ' + stri[2] + ' ' + stri[3], '+', stri[6]]
    return res


def write_csv_file(url: str):
    file = ur.urlopen(url)
    leng = 0
    for line in file:
        if line.decode('utf-8').strip().split()[0] == 'РK:':
            leng += 1
    res = read_input_file(url, leng)
    for i, val in enumerate(res):
        res[i] = ','.join(val)
    with open('../total.csv', 'w') as file:
        for i in res:
            file.write(i + '\n')
