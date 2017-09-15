"""
You are given the following information,
but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4,
but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""


def main():
    count = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if get_week(year, month, 1) == 'Sunday':
                count += 1
    print(count)


def is_leap(year):
    if year % 100 == 0:
        if year // 400 == year / 400:
            return True
    else:
        if year // 4 == year / 4:
            return True
    return False


def get_week(year, month, day):
    weekdays = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_not_leap = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    distance = 0
    for i in range(1900, year + 1):
        if is_leap(year):
            distance += 366
        else:
            distance += 365
    for i in range(month):
        if is_leap(year):
            distance += days_leap[i]
        else:
            distance += days_not_leap[i]
    distance += day
    return weekdays[distance % 7]


if __name__ == '__main__':
    # main()
    print(get_week(1901, 1, 1))
