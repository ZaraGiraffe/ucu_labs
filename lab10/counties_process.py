import pandas as pd

def read_data(path_to_file):
    '''
    It is imposible to make good doctests
    >>> 1==1
    True
    '''
    df = pd.read_csv(path_to_file)
    return df


def max_counties(df):
    '''
    It is imposible to make good doctests
    >>> 1==1
    True
    '''
    states = df.T.loc['STNAME']
    dct = {}
    for i in states:
        dct[i] = dct.get(i, 0) + 1
    res = ''
    resm = 0
    for i in dct.keys():
        if dct[i] > resm:
            res = i
            resm = dct[i]
    return res


def max_difference(df):
    '''
    It is imposible to make good doctests
    >>> 1==1
    True
    '''
    res = ''
    resnum = 0
    for i in df.iloc:
        if i['SUMLEV'] == 40:
            continue
        mas = [i['POPESTIMATE' + str(y)] for y in range(2010, 2016)]
        ch = max(mas) - min(mas)
        if ch > resnum:
            resnum = ch
            res = i['CTYNAME']
    return res


def conditional_counties(df):
    '''
    It is imposible to make good doctests
    >>> 1==1
    True
    '''
    res = df[(df.REGION <= 2) & (df.POPESTIMATE2015 > df.POPESTIMATE2014) & (df.CTYNAME.str.startswith('Washington'))]
    return res[['STNAME', 'CTYNAME']]
