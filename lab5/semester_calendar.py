from datetime import date


months = ["January", "February", "March", "April", "May", "June", \
    "July", "August", "September", "October", "Novermber", "December"]
months_len = ["31", "28", "31", "30", "31", "30", \
    "31", "31", "30", "31", "30", "31"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
clas_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
con1 = "&nbsp"
con2 = "noday"
con3 = '<tr><th class="mon">Mon</th><th class="tue">Tue</th><th \
class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th>\
<th class="sat">Sat</th><th class="sun">Sun</th></tr>'


def txt_calendar(year, first_month):
    dat = date(year, first_month, 1)
    day = dat.weekday()
    strings = ""
    strings += f"{months[first_month-1] + ' ' + str(year):^21}" + '\n'
    for i in days:
        strings += i[:2] + ' '
    strings += '\n'
    mystr = ""
    for i in range(day):
        mystr += f"{' ':>3}"
    for i in range(1, int(months_len[first_month-1])+1):
        mystr += f"{i:<3}"
        day += 1
        if day == 7:
            strings += mystr
            if i != int(months_len[first_month-1]):
                strings += '\n'
            day = 0
            mystr = ''
    strings += mystr
    return strings


def html_calendar(year, first_month):
    tr1 = "<tr>"
    tr2 = "</tr>"
    k1 = "<td class=\""
    k2 = "\">"
    k3 = "</td>"
    s1 = '<table border="0" cellpadding="0" cellspacing="0" class="month">'
    s2 = '</table>'
    m1 = '<tr><th colspan="7" class="month">'
    m2 = '</th></tr>'
    dat = date(year, first_month, 1)
    day = dat.weekday()
    fstr = m1 + months[first_month-1] + ' ' + str(year) + m2
    strings = s1 + '\n' + fstr + '\n' + con3 + '\n'
    mystr = tr1
    for i in range(day):
        mystr += k1 + con2 + k2 + con1 + k3
    for i in range(1, int(months_len[first_month-1])+1):
        mystr += k1 + clas_days[day] + k2 + str(i) + k3
        day += 1
        if day == 7:
            mystr += tr2
            strings += mystr + '\n'
            mystr = tr1
            day = 0
    if day != 0:
        while day != 7:
            mystr += k1 + con2 + k2 + con1 + k3
            day += 1
        mystr += tr2
        strings += mystr + '\n'
    strings += s2
    return strings


def semester_calendar(output_type, year, first_month, last_month):
    """
    >>> semester_calendar('txt', 2004, 2, 5)
    '    February 2004    \\nMo Tu We Th Fr Sa Su \\n                  1  \\n2  3  4  5  6  7  8  \\n9  10 11 12 13 14 15 \\n16 17 18 19 20 21 22 \\n23 24 25 26 27 28 \\n     March 2004      \\nMo Tu We Th Fr Sa Su \\n1  2  3  4  5  6  7  \\n8  9  10 11 12 13 14 \\n15 16 17 18 19 20 21 \\n22 23 24 25 26 27 28 \\n29 30 31 \\n     April 2004      \\nMo Tu We Th Fr Sa Su \\n         1  2  3  4  \\n5  6  7  8  9  10 11 \\n12 13 14 15 16 17 18 \\n19 20 21 22 23 24 25 \\n26 27 28 29 30 \\n      May 2004       \\nMo Tu We Th Fr Sa Su \\n               1  2  \\n3  4  5  6  7  8  9  \\n10 11 12 13 14 15 16 \\n17 18 19 20 21 22 23 \\n24 25 26 27 28 29 30 \\n31 '
    >>> semester_calendar('html', 2004, 2, 5)
    '<table border="0" cellpadding="0" cellspacing="0" class="month">\\n<tr><th colspan="7" class="month">February 2004</th></tr>\\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>\\n<tr><td class="noday">&nbsp</td><td class="noday">&nbsp</td><td class="noday">&nbsp</td><td class="noday">&nbsp</td><td class="noday">&nbsp</td><td class="noday">&nbsp</td><td class="Sun">1</td></tr>\\n<tr><td class="Mon">2</td><td class="Tue">3</td><td class="Wed">4</td><td class="Thu">5</td><td class="Fri">6</td><td class="Sat">7</td><td class="Sun">8</td></tr>\\n<tr><td class="Mon">9</td><td class="Tue">10</td><td class="Wed">11</td><td class="Thu">12</td><td class="Fri">13</td><td class="Sat">14</td><td class="Sun">15</td></tr>\\n<tr><td class="Mon">16</td><td class="Tue">17</td><td class="Wed">18</td><td class="Thu">19</td><td class="Fri">20</td><td class="Sat">21</td><td class="Sun">22</td></tr>\\n<tr><td class="Mon">23</td><td class="Tue">24</td><td class="Wed">25</td><td class="Thu">26</td><td class="Fri">27</td><td class="Sat">28</td><td class="noday">&nbsp</td></tr>\\n</table>\\n<table border="0" cellpadding="0" cellspacing="0" class="month">\\n<tr><th colspan="7" class="month">March 2004</th></tr>\\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>\\n<tr><td class="Mon">1</td><td class="Tue">2</td><td class="Wed">3</td><td class="Thu">4</td><td class="Fri">5</td><td class="Sat">6</td><td class="Sun">7</td></tr>\\n<tr><td class="Mon">8</td><td class="Tue">9</td><td class="Wed">10</td><td class="Thu">11</td><td class="Fri">12</td><td class="Sat">13</td><td class="Sun">14</td></tr>\\n<tr><td class="Mon">15</td><td class="Tue">16</td><td class="Wed">17</td><td class="Thu">18</td><td class="Fri">19</td><td class="Sat">20</td><td class="Sun">21</td></tr>\\n<tr><td class="Mon">22</td><td class="Tue">23</td><td class="Wed">24</td><td class="Thu">25</td><td class="Fri">26</td><td class="Sat">27</td><td class="Sun">28</td></tr>\\n<tr><td class="Mon">29</td><td class="Tue">30</td><td class="Wed">31</td><td class="noday">&nbsp</td><td class="noday">&nbsp</td><td class="noday">&nbsp</td><td class="noday">&nbsp</td></tr>\\n</table>\\n<table border="0" cellpadding="0" cellspacing="0" class="month">\\n<tr><th colspan="7" class="month">April 2004</th></tr>\\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>\\n<tr><td class="noday">&nbsp</td><td class="noday">&nbsp</td><td class="noday">&nbsp</td><td class="Thu">1</td><td class="Fri">2</td><td class="Sat">3</td><td class="Sun">4</td></tr>\\n<tr><td class="Mon">5</td><td class="Tue">6</td><td class="Wed">7</td><td class="Thu">8</td><td class="Fri">9</td><td class="Sat">10</td><td class="Sun">11</td></tr>\\n<tr><td class="Mon">12</td><td class="Tue">13</td><td class="Wed">14</td><td class="Thu">15</td><td class="Fri">16</td><td class="Sat">17</td><td class="Sun">18</td></tr>\\n<tr><td class="Mon">19</td><td class="Tue">20</td><td class="Wed">21</td><td class="Thu">22</td><td class="Fri">23</td><td class="Sat">24</td><td class="Sun">25</td></tr>\\n<tr><td class="Mon">26</td><td class="Tue">27</td><td class="Wed">28</td><td class="Thu">29</td><td class="Fri">30</td><td class="noday">&nbsp</td><td class="noday">&nbsp</td></tr>\\n</table>\\n<table border="0" cellpadding="0" cellspacing="0" class="month">\\n<tr><th colspan="7" class="month">May 2004</th></tr>\\n<tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>\\n<tr><td class="noday">&nbsp</td><td class="noday">&nbsp</td><td class="noday">&nbsp</td><td class="noday">&nbsp</td><td class="noday">&nbsp</td><td class="Sat">1</td><td class="Sun">2</td></tr>\\n<tr><td class="Mon">3</td><td class="Tue">4</td><td class="Wed">5</td><td class="Thu">6</td><td class="Fri">7</td><td class="Sat">8</td><td class="Sun">9</td></tr>\\n<tr><td class="Mon">10</td><td class="Tue">11</td><td class="Wed">12</td><td class="Thu">13</td><td class="Fri">14</td><td class="Sat">15</td><td class="Sun">16</td></tr>\\n<tr><td class="Mon">17</td><td class="Tue">18</td><td class="Wed">19</td><td class="Thu">20</td><td class="Fri">21</td><td class="Sat">22</td><td class="Sun">23</td></tr>\\n<tr><td class="Mon">24</td><td class="Tue">25</td><td class="Wed">26</td><td class="Thu">27</td><td class="Fri">28</td><td class="Sat">29</td><td class="Sun">30</td></tr>\\n<tr><td class="Mon">31</td><td class="noday">&nbsp</td><td class="noday">&nbsp</td><td class="noday">&nbsp</td><td class="noday">&nbsp</td><td class="noday">&nbsp</td><td class="noday">&nbsp</td></tr>\\n</table>'
    """
    if output_type == "txt":
        string = ''
        for i in range(first_month, last_month + 1):
            string += txt_calendar(year, i)
            if i != last_month:
                string += '\n'
        return string
    if output_type == "html":
        string = ''
        for i in range(first_month, last_month + 1):
            string += html_calendar(year, i)
            if i != last_month:
                string += '\n'
        return string
