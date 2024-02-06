import datetime


def time_now():
    now = datetime.datetime.now()
    date_time = (now.strftime('%Y-%m-%d_%H:%M:%S'))
    date1 = (now.date())
    return date_time, date1


date_time, date_o = time_now()
print("полная дата и время текущего момента")
print(f'{date_time} длинна {len(date_time)}')
print("дата текущего момента")
print(f'{date_o}          длинна {len(str(date_o))}')
