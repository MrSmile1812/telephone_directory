from rich.console import Console
from support_functions import (
    check_correct_row_to_edit,
    check_count,
    check_is_letters,
    check_is_phone_number,
    check_number_of_rows,
    check_position,
    create_table,
)


console = Console()


def show():
    '''Функция позволяет отобразить определнное кол-во контактов в таблице.'''
    count = check_count()
    if count is False:
        return
    table = create_table()
    position = check_position(count)
    rows = check_number_of_rows(position, count)
    with open('telephone_directory.txt', encoding='utf-8') as file:
        data = file.readlines()
        for item in range(position, rows):
            row = data[item].rstrip("\n").split(',')
            table.add_row(
                str(item + 1), row[0], row[1], row[2], row[3], row[4], row[5]
            )
    console.print(table)
    console.print(f'Показаны с {position + 1} по {rows} из {count}')


def add():
    '''Функция позволяет добавить новый контакт в таблицу.'''
    count = check_count()
    table = create_table()
    second_name = check_is_letters('Введите фамилию - ')
    first_name = check_is_letters('Введите имя - ')
    patronymic = check_is_letters('Введите отчество - ')
    organization = input('Введите организацию - ')
    tel = check_is_phone_number('Введите рабочий - ')
    mob = check_is_phone_number('Введите мобильный - ')
    with open('telephone_directory.txt', "a+", encoding='utf-8') as file:
        if count != 0:
            file.write('\n')
        file.write(
            f'{second_name},{first_name},{patronymic},'
            f'{organization},{tel},{mob}'
        )
    table.add_row(
        str(count + 1), second_name, first_name,
        patronymic, organization, tel, mob
    )
    console.print(table)


def edit():
    '''Функция позволяет отредактировать определенный контакт в таблице.'''
    count = check_count()
    if count is False:
        return
    table = create_table()
    number_of_row = check_correct_row_to_edit() - 1
    with open('telephone_directory.txt', 'r') as file:
        old_data_replace = file.read()
    with open('telephone_directory.txt', 'r') as file:
        old_data = file.readlines()
    old_row = old_data[number_of_row]
    view_old_row = old_row.rstrip("\n").split(',')
    table.add_row(
        str(number_of_row + 1), view_old_row[0], view_old_row[1],
        view_old_row[2], view_old_row[3], view_old_row[4], view_old_row[5]
    )
    console.print(table)
    table = create_table()
    second_name = check_is_letters('Введите фамилию - ')
    first_name = check_is_letters('Введите имя - ')
    patronymic = check_is_letters('Введите отчество - ')
    organization = input('Введите организацию - ')
    tel = check_is_phone_number('Введите рабочий - ')
    mob = check_is_phone_number('Введите мобильный - ')
    if number_of_row + 1 == count:
        new_row = ','.join(
            [second_name, first_name, patronymic, organization, tel, mob]
        )
    else:
        new_row = ','.join(
            [second_name, first_name, patronymic, organization, tel, mob, '\n']
        )
    new_data = old_data_replace.replace(old_row, new_row)
    with open('telephone_directory.txt', 'w') as file:
        file.write(new_data)
    view_new_row = new_row.rstrip("\n").split(',')
    table.add_row(
        str(number_of_row + 1), view_new_row[0], view_new_row[1],
        view_new_row[2], view_new_row[3], view_new_row[4], view_new_row[5]
    )
    console.print(table)


def search():
    '''Функция позволяет найти контакты с заданным значением.'''
    count = check_count()
    if count is False:
        return
    table = create_table()
    counter = 0
    search_data = input('Напишите искомое значение - ')
    with open('telephone_directory.txt', encoding='utf-8') as file:
        data = file.readlines()
        for item in range(count):
            row = data[item]
            if search_data in row:
                row = row.rstrip("\n").split(',')
                table.add_row(
                    str(item + 1), row[0], row[1],
                    row[2], row[3], row[4], row[5]
                )
                counter += 1
    if counter > 0:
        console.print(table)
    else:
        print('Данных не обнаружено.')


def exit():
    '''Функция выхода из программы.'''
    print('До свидания!')


def help():
    '''Функция для помощи пользовтелю.'''
    print('show - отображение книги номеров;',
          'add - добавить новую строку;',
          'edit - редактировать существующую строку;',
          'search - найти строку;',
          'exit - чтобы выйти.',
          sep='\n')


def main() -> str:
    if __name__ == '__main__':
        print('Здравствуйте! Я Ваш личный телефонный справочник. \n'
              'Введите команду "help", чтобы узнать, на что я способен '
              'или "exit", чтобы выйти.\n')
        commands = {
            'show': show,
            'add': add,
            'edit': edit,
            'search': search,
            'help': help,
            'exit': exit,
        }
        cmd = None
        while cmd != 'exit':
            cmd = input('Введите команду: ')
            if cmd not in commands:
                print('Команда введена некорректно. \n'
                      'Чтобы увидеть список команд, напишите "help".\n')
            else:
                commands.get(cmd)()


main()
