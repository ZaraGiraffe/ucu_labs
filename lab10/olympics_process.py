from os import read
import pandas as pd
from pandas.core.frame import DataFrame


def read_data():
    '''
    It is imposible to make good doctests
    >>> 1==1
    True
    '''
    df = pd.read_csv('olympics.csv', index_col=0, skiprows=1)
    for col in df.columns:
        if col[:2] == '01':
            df.rename(columns={col: 'Gold'+col[4:]}, inplace=True)
        elif col[:2] == '02':
            df.rename(columns={col: 'Silver'+col[4:]}, inplace=True)
        elif col[:2] == '03':
            df.rename(columns={col: 'Bronze'+col[4:]}, inplace=True)
        elif col[:1] == '№':
            df.rename(columns={col: '#'+col[1:]}, inplace=True)

    names_ids = df.index.str.split('\\s\\(') # split the index by '('

    df.index = names_ids.str[0] # the [0] element is the country name (new index)
    df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

    df = df.drop('Totals')
    #print(df)

    return df


def first_country(df):
    '''
    It is imposible to make good doctests
    >>> 1==1
    True
    '''
    return df.iloc[0]


def summer_biggest(df: DataFrame):
    '''
    It is imposible to make good doctests
    >>> 1==1
    True
    '''
    res = df.iloc[0]
    for i in df.iloc:
        if i['Gold'] > res['Gold']:
            res = i
    return res.name


def difference_biggest(df):
    '''
    It is imposible to make good doctests
    >>> 1==1
    True
    '''
    res = df.iloc[0]
    for i in df.iloc:
        if abs(i['Gold'] - i['Silver']) > abs(res['Gold'] - res['Silver']):
            res = i
    return res.name


def difference_biggest_relative(df):
    '''
    It is imposible to make good doctests
    >>> 1==1
    True
    '''
    res = df.iloc[0]
    res['Gold'] = res['Gold.1'] = 1
    for i in df.iloc:
        if i['Gold'] == 0 or i['Gold.1'] == 0:
            continue
        if abs(i['Gold'] - i['Gold.1']) / (i['Gold'] + i['Gold.1']) > abs(res['Gold'] - res['Gold.1']) / (res['Gold'] + res['Gold.1']):
            res = i
    return res.name


def get_points(df):
    '''
    It is imposible to make good doctests
    >>> 1==1
    True
    '''
    df['Points'] = (df['Gold'] + df['Gold.1']) * 3 + (df['Silver'] + df['Silver.1']) * 2 + (df['Bronze'] + df['Bronze.1'])
    return df['Points']
