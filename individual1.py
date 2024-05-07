"""
Для своего варианта лабораторной работы 2.8 необходимо дополнительно реализовать
сохранение и чтение данных из файла формата JSON. Необходимо также проследить за тем,
чтобы файлы генерируемый этой программой не попадали в репозиторий лабораторной
работы.
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


def add_train(trains):
    """Добавляет информацию о поезде."""
    destination = input("Название пункта назначения: ")
    train_number = input("Номер поезда: ")
    departure_time = input("Время отправления (в формате ЧЧ:ММ): ")

    train = {
        'название пункта назначения': destination,
        'номер поезда': train_number,
        'время отправления': departure_time,
    }

    trains.append(train)
    trains.sort(key=lambda x: x['название пункта назначения'])


def list_trains(trains):
    """Выводит список всех поездов."""
    line = f'+-{"-" * 35}-+-{"-" * 15}-+-{"-" * 25}-+'
    print(line)
    print(f"| {'Название пункта назначения':^35} | {'Номер поезда':^15} | {'Время отправления':^25} |")

    for train in trains:
        print(line)
        print(
            f"| {train['название пункта назначения']:^35} | {train['номер поезда']:^15} | {train['время отправления']:^25} |")
    print(line)


def select_trains(trains, search_time):
    """Выводит поезда, отправляющиеся после указанного времени."""
    found = False
    result = []

    print(f"Поезда, отправляющиеся после {search_time}:")
    for train in trains:
        train_time = train['время отправления']
        if train_time >= search_time:
            result.append(train)
            found = True
    if found:
        return result

    if not found:
        return "Нет поездов, отправляющихся после указанного времени."


def display_help():
    """Выводит справку о доступных командах."""
    print("Список команд:\n")
    print("add - добавить информацию о поезде;")
    print("list - вывести список всех поездов;")
    print("select <время> - вывести поезда, отправляющиеся после указанного времени;")
    print("save <file_name> - сохранить информацию о поездах в файл JSON;")
    print("load <file_name> - загрузить информацию о поездах из файла JSON;")
    print("exit - завершить работу с программой.")


def save_trains(file_name, trains):
    """
    Сохранить информацию о поездах в файл JSON.
    """
    with open(file_name, "w", encoding="utf-8") as fout:
        # Выполнить сериализацию данных в формат JSON.
        # Для поддержки кириллицы установим ensure_ascii=False
        json.dump(trains, fout, ensure_ascii=False, indent=4)
        print(f"Данные о поездах сохранены в файл {file_name}")


def load_trains(file_name):
    """
    Загрузить информацию о поездах из файла JSON.
    """
    try:
        # Открыть файл с заданным именем для чтения.
        with open(file_name, "r", encoding="utf-8") as fin:
            # Выполнить десериализацию данных из формата JSON.
            loaded_trains = json.load(fin)
            return loaded_trains
    except FileNotFoundError:
        print(f"Файл {file_name} не найден.")
        return []


def main():
    """Основная функция управления программой."""
    trains = []

    while True:
        command = input(">>> ").lower().split()

        if not command:
            continue

        if command[0] == 'exit':
            break
        elif command[0] == 'add':
            add_train(trains)
        elif command[0] == 'list':
            list_trains(trains)
        elif command[0] == 'select':
            if len(command) != 2:
                print("Некорректное количество аргументов для команды 'select'.")
                continue
            selected = select_trains(trains, command[1])
            list_trains(selected)
        elif command[0] == 'save':
            if len(command) != 2:
                print("Некорректное количество аргументов для команды 'save'.")
                continue
            save_trains(command[1], trains)
        elif command[0] == 'load':
            if len(command) != 2:
                print("Некорректное количество аргументов для команды 'load'.")
                continue
            trains = load_trains(command[1])
        elif command[0] == 'help':
            display_help()
        else:
            print(f"Неизвестная команда {command[0]}")


if __name__ == '__main__':
    main()
