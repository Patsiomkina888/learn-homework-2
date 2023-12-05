"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

user_list = [
    {"name": "Маша", "age": 25, "job": "Scientist"},
    {"name": "Вася", "age": 8, "job": "Programmer"},
    {"name": "Эдуард", "age": 48, "job": "Big boss"},
    {"name": "Иннокентий", "age": 75, "job": "Enthusiast"},
]


def main():
    with open("user_list.csv", "w", encoding="utf-8") as f:
        fields = ["name", "job", "age"]
        writer = csv.DictWriter(f, fields, delimiter=";")
        writer.writeheader()
        for user in user_list:
            writer.writerow(user)


if __name__ == "__main__":
    main()
