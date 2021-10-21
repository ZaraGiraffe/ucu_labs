import doctest, datetime


def weekday_name(number: int) -> str:
    """
    Return a string representing a weekday
    (one of "mon", "tue", "wed", "thu", "fri", "sat", "sun")
    number : an integer in range [0, 6]
        
    >>> weekday_name(3)
    'thu'
    """
    con = ("mon", "tue", "wed", "thu", "fri", "sat", "sun")
    return con[number]

	
def weekday(date: str) -> int:
    """
    Return an integer representing a weekday
    (0 represents monday and so on)
    Read about algorithm as Zeller's Congruence
    date : a string of form "day.month.year
    if the date is invalid raises AssertionError 
    with corresponding message

    >>> weekday("12.08.2015")
    2
    >>> weekday("28.02.2016")
    6
    """
    date = date.split('.')
    for i in range(len(date)):
        date[i] = int(date[i])
    if date[0] < 1 or date[1] < 1 or date[0] > 31 or date[1] > 12:
        raise AssertionError
    return datetime.datetime(date[2], date[1], date[0]).weekday()


def calendar(month: int, year: int) -> str:
    """Return a string representing a
    horizontal calendar for the given month and year.

    month : an integer in range [1 , 12]
    year : an integer (strictly speaking the algorithm in weekday
           works correctly only for Gregorian calendar, so year must
           be greater than 1583)
    when arguments are invalid raises AssertionError with corresponding
    message

    >>> print(calendar(8 , 2015))
    mon tue wed thu fri sat sun
                          1   2
      3   4   5   6   7   8   9
     10  11  12  13  14  15  16
     17  18  19  20  21  22  23
     24  25  26  27  28  29  30
     31
    """
    if not isinstance(month, int) or not isinstance(year, int) or month < 1 or month > 12:
        raise AssertionError
    con = "mon tue wed thu fri sat sun\n"
    import calendar
    y = calendar.month(year, month).strip().split('\n')
    cal = []
    for i in y[2:]:
        cal.append(i.strip().split())
    for v, i in enumerate(cal):
        if len(i) < 7:
            newi = [-1 for j in range(7-len(i))]
            if i[0] == '1':
                newi.extend(i)
                cal[v] = newi
    res = con
    for v, i in enumerate(cal):
        ins  = ''
        for ch, j in enumerate(i):
            if j == -1:
                ins += "   "
            else:
                ins += f"{j:>3}"
            if ch != len(i) - 1:
                ins += ' '
            else:
                if v != len(cal)-1:
                    ins += '\n'
        res += ins
    return res


def transform_calendar(calendar: str) -> str:
    """Return a modified horizontal -> vertical calendar.

    calendar is a string of a calendar, returned by the calendar()
    function.
    >>> print(transform_calendar(calendar(5, 2002)))
    mon   6 13 20 27
    tue   7 14 21 28
    wed 1 8 15 22 29
    thu 2 9 16 23 30
    fri 3 10 17 24 31
    sat 4 11 18 25
    sun 5 12 19 26
    >>> print(transform_calendar(calendar(8 , 2015)))
    mon   3 10 17 24 31
    tue   4 11 18 25
    wed   5 12 19 26
    thu   6 13 20 27
    fri   7 14 21 28
    sat 1 8 15 22 29
    sun 2 9 16 23 30
    """
    con = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    y = calendar.strip().split('\n')
    cal = []
    for i in y[1:]:
        cal.append(i.strip().split())
    for v, i in enumerate(cal):
        if len(i) < 7:
            newi = [-1 for j in range(7-len(i))]
            newj = [-2 for j in range(7-len(i))]
            if i[0] == '1':
                newi.extend(i)
            else:
                newi = i + newj
            cal[v] = newi
    res = ''
    for i in range(7):
        ins = con[i]
        for j in cal:
            if j[i] == -1:
                ins += '  '
            elif j[i] == -2:
                continue
            else:
                ins += ' ' + j[i]
        if i != 6:
            ins += '\n'
        res += ins
    return res


if __name__ == '__main__':
    try:
        print("Type month")
        month = input()
        month = int(month)
        print("Type year")
        year = input()
        year = int(year)
        print("\n\nThe calendar is: ")
        print (calendar(month, year))
    except ValueError as err:
        print(err)
