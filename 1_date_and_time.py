"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, timedelta


def print_days():
    dt_now = datetime.now()
    print(dt_now)
    print(dt_now - timedelta(days=1))
    print(dt_now + timedelta(days=30))
    return


def str_2_datetime(date_string):
    try:
        return datetime.strptime(date_string, "%m/%d/%y  %H:%M:%S.%f")
    except ValueError:
        return "Некорректный формат даты"


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
