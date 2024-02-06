import datetime

def print_to_file(text: str) -> None:
    date_time, date = time_now()
    # file_name = date_time + ".txt"
    file = open('тест на русский.txt', 'a+', encoding='utf-8')
    print(date_time, text, file=file)
    file.close()  # закрыть файл после работы с ним.

def time_now():
    ''' получение текущего времени и даты. Отдаёт формирование имени файла'''
    now = datetime.datetime.now()
    date_time_now = (now.strftime('%Y-%m-%d %H°%M\'\'%S\''))  # '%Y-%m-%d %H:%M:%S'
    date = (now.date())
    return date_time_now, date

print_to_file("проба")