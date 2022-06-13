import datetime as dt

now = dt.datetime.now()


def creat_Path(now):
    now = now
    t_month = ""
    t_day = ""
    t_minute = ""

    if now.month < 10:
        t_month = '0' + str(now.month)

    if now.day < 10:
        t_day = '0' + str(now.day)
    else:
        t_day = str(now.day)

    if now.minute < 10:
        t_minute = '0' + str(now.minute)
    else:
        t_minute = str(now.minute)

    t_hm = ""

    if now.hour > 12 and now.hour <= 23:
        t_hm = "오후 " + str(now.hour - 12) + '_' + str(t_minute)
    elif now.hour == 12:
        t_hm = "오후 " + str(now.hour) + '_' + str(t_minute)
    elif now.hour == 0:
        t_hm = "오전 " + str(now.hour + 12) + '_' + str(t_minute)
    else:
        t_hm = "오전 " + str(now.hour) + '_' + str(t_minute)

    t_date = str(now.year) + '-' + str(t_month) + '-' + str(t_day) + '_' + t_hm

    return t_date
