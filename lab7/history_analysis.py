from get_browser_history import get_chrome_os


def sites_on_date(visits: list, date: str):
    """
    Returns set of all urls that have been visited
    on current date
    :param visits: all visits in browser history
    :param date: date in format "yyyy-mm-dd"
    :return: set of url visited on date
    """
    res = set()
    for i in visits:
        if date in i:
            res.add(i[0])
    return res


def most_frequent_sites(visits: list, number: int):
    """
    Returns set of most frequent sites visited in total
    Return only 'number' of most frequent sites visited
    :param visits: all visits in browser history
    :param number: number of most frequent sites to return
    :return: set of most frequent sites
    """
    dct = {}
    for i in visits:
        dct[i[0]] = dct.get(i[0], 0) + 1
    newdct = []
    for k, v in dict.items():
        newdct.append((v, k))
    newdct.sort()
    newdct.reverse()
    res = set()
    for i in newdct:
        if number == 0:
            break
        res.add(i[1])
        number -= 1
    return res


def get_url_info(visits: list, url: str):
    """
    Returns tuple with info about site, which title is passed
    Function should return:
    title - title of site with this url
    last_visit_date - date of the last visit of this site, in format "yyyy-mm-dd"
    last_visit_time - time of the last visit of this site, in format "hh:mm:ss.ms"
    num_of_visits - how much time was this site visited
    average_time - average time, spend on this site
    :param visits: all visits in browser history
    :param url: url of site to search
    :return: (title, last_visit_date, last_visit_time, num_of_visits, average_time)
    """
    count = 0
    lst_time = []
    res = ('nothing', '0000-00-00', '00:00:00.00', 0, 0)
    for i in visits:
        if url == i[0]:
            res[0] = i[1]
            count += 1
            lst_time.append(i[4])
            if i[2] > res[1]:
                res[1] = i[2]
                res[2] = i[3]
            elif i[2] == res[1]:
                if i[3] > res[2]:
                    res[2] = i[3]
    res[3] = count
    if len(lst_time) > 0:
        res[4] = sum(lst_time) / len(lst_time)
    return res
