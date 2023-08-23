import re
import os
from rich.table import Table


def check_count():
    '''Открытие файла или создание нового, если его не существует.
    Проверка файла на пустоту или возвращение кол-ва строк.'''
    if os.path.isfile('telephone_directory.txt'):
        with open('telephone_directory.txt', encoding='utf-8') as file:
            for count, line in enumerate(file):
                pass
    else:
        with open('telephone_directory.txt', 'w', encoding='utf-8') as file:
            pass
    if os.path.getsize('telephone_directory.txt') == 0:
        print('В файле нет данных.')
        return False
    else:
        count += 1
        return count


def check_number_of_rows(position, count):
    '''Проверка на валидность при кол-ве запрашиваемых строк.'''
    while True:
        number_of_rows = int(
            input('Сколько строк отображать на странице? - ')
        )
        rows = position + number_of_rows
        if number_of_rows < 1:
            print('Введите корректное кол-во.')
            continue
        elif count < rows:
            print(f'Требуемое кол-во больше, чем есть в базе данных. \n'
                  f'Будут показаны данные с {position + 1} по последнюю.')
            rows = count
            return rows
        else:
            return rows


def check_position(count):
    '''Проверка наличия выбранной строки.'''
    while True:
        position = int(
            input(f'Всего в базе данных {count} номеров.\n'
                  'С какой позиции отобразить данные? - ')
            ) - 1
        if position + 1 > 0 and position < count:
            return position
        else:
            print('Введите корректную позицию.')
            continue


def create_table():
    '''Создание формы таблицы для отображения её в консоли.'''
    columns = [
        '#', 'Фамилия', 'Имя', 'Отчество',
        'Организация', 'Рабочий', 'Мобильный'
    ]
    table = Table(title='Телефонный справочник')
    for column in columns:
        table.add_column(column, justify='center')
    return table


def check_is_letters(field):
    '''Проверка на верный ввод данных - буквы.'''
    while True:
        data = input(f"{field}")
        if data.isalpha() and len(data) != 0:
            return data
        else:
            print('Неверный формат ввода данных! \n'
                  'Строка должна состоять из букв.')
            continue


def check_is_phone_number(field):
    '''Проверка на верный ввод данных - номер телефона.'''
    while True:
        data = ''.join(input(field).split())
        rule = "^\\+?[1-9][0-9]{7,14}$"
        if re.match(rule, data):
            return data
        else:
            print('Неверный формат ввода данных! \n'
                  'Строка должна быть в формате: +X X XXX XXX XXX '
                  'или X XXX XXX XX XX.')
            continue


def check_correct_row_to_edit():
    '''Проверка на корректный номер искомой строки.'''
    count = check_count()
    while True:
        number_of_row = input(
            'Укажите номер строки, которую хотите изменить - '
        )
        if number_of_row.isdigit() and int(number_of_row) <= count:
            return int(number_of_row)
        else:
            print('Указан неккоректный номер строки.')
