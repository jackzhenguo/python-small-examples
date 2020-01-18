from datetime import date, datetime
import calendar


def print_mydate(mydate):
    print(f'输入的日期:{mydate}\n')

    year_calendar_str = calendar.calendar(mydate.year)
    print(f"{mydate.year}年的日历图：{year_calendar_str}\n")

    is_leap = calendar.isleap(mydate.year)
    print_leap_str = "%s年是闰年" if is_leap else "%s年不是闰年\n"
    print(print_leap_str % mydate.year)

    month_calendar_str = calendar.month(mydate.year, mydate.month)
    print(f"{mydate.year}年-{mydate.month}月的日历图：{month_calendar_str}\n")

    weekday, days = calendar.monthrange(mydate.year, mydate.month)
    print(f'{mydate.year}年-{mydate.month}月的第一天是那一周的第{weekday}天\n')
    print(f'{mydate.year}年-{mydate.month}月共有{days}天\n')

    month_first_day = date(mydate.year, mydate.month, 1)
    print(f"当月第一天:{month_first_day}\n")

    month_last_day = date(mydate.year, mydate.month, days)
    print(f"当月最后一天:{month_last_day}\n")


print_mydate(date.today())
