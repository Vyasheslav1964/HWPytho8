# №55. Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

# Этапы работы:

# 1) Создать телефонный справочник:
#     - Открыть файл в режиме добавления (а)
# 2) Добавить контакт:
#     - Запросить информацию у пользователя
#     - Добавить информацифю в необходимом формате
#     - Открыть файл в режиме добавления (а)
#     - Добавить контакт в файл
# 3) Вывести данные из файла на экран:
#     - Открыть файл в режиме чтения (r)
#     - Вывусти информацию на экран
# 4) Поиск данных : 
#     - Запросить вариант поиска
#     - Запросить данные поиска
#     - Открыть файл в режиме чтения (r)
#     - Сохранить данные в переменную
#     - Осуществить поиск по файлу
#     - Вывести информацию на экран
# 5) Реализовать UI :
#     - Вывести варианта меню
#     - Получение запроса пользователя
#     - Реализация запроса пользователя
#     - Выход из программы
# 6) Дополнить справочник возможностью копирования данных из одного файла в другой.
#    Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
#     - Запросить информацию у пользователя
#     - Добавить информацифю в необходимом формате
#     - Открыть файл в режиме добавления (а)
#     - Добавить контакт в файл

def input_name():
    return input('Введите имя : ')

def input_surname():
    return input('Введите фамилию : ')

def input_patronymic():
    return input('Введите отчество : ')

def input_phone():
    return input('Введите номер телефона : ')

def input_address():
    return input('Введите адрес : ')

def number_str():
    return input('Введите номер строки которую надо сохранить: ')

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic() 
    phone = input_phone()
    address = input_address()
    return f'{surname} {name}  {patronymic}  {phone} \n'f'{address}\n\n'


def add_contact(contact):
    
    with open('phonebook.txt', 'a', encoding= 'UTF-8') as file:
        file.write(contact)

def show_info():
    with open('phonebook.txt', 'r', encoding= 'UTF-8') as file:
            contacts_list = file.read().rstrip().split('\n\n')
            # print(file.read().rstrip())
            new_contact = ()
            for  contact in enumerate(contacts_list, 1):
                print(*contact)
                new_contact = new_contact + contact

    copy_contact = int(number_str())
    #print(copy_contact)
    list_len = [i for i in range(1, len(new_contact)//2 + 1)]
    print(list_len)
    while copy_contact not in list_len:
            print('Такой строки нет')
            copy_contact = int(number_str())
    if copy_contact == 1:
       # print(str(new_contact[copy_contact-1]) + ' ' + str(new_contact[copy_contact ]))
        copy_fail = str(new_contact[copy_contact-1]) + ' ' + str(new_contact[copy_contact ])
    elif copy_contact == 2:
        #print(str(new_contact[copy_contact]) + ' ' + str(new_contact[copy_contact +1]))
        copy_fail = str(new_contact[copy_contact]) + ' ' + str(new_contact[copy_contact +1])
    else:
        # print(str(copy_contact) + ' ' + str(new_contact[copy_contact*2+1]))
        copy_fail = str(copy_contact) + ' ' + str(new_contact[copy_contact*2-1])
    print(copy_fail)
    with open('copy.txt', 'a', encoding= 'UTF-8') as file:
        file.write(str(copy_fail) +'\n')
            
def search_contact():
    var_search = input('Выберите вариант поиска: \n'
                       '1. По фамилии\n'
                       '2. По имени\n'
                       '3. По отчеству\n'
                       '4. По номеру телефона\n'
                       '5. По адресу\n'
                       'Ввод: ')
    while var_search not in ('1', '2', '3', '4', '5'):
            print('Некорректные данные, нужно ввести число комманды')
            var_search = input('Введите вариант поиска: ')

    index_var = int(var_search) -1
    
    search = input('Введите данные для поиска: ')

    with open('phonebook.txt', 'r', encoding= 'UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
    # print(contacts_list)
    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n', ' ').split()
        if search in contact_lst[index_var]:
            print(contact_str)
 
def interface():
    with open('phonebook.txt', 'a', encoding= 'UTF-8'):
        pass
    command = '-1'
    while command != '4':
        print('Возможные варианты взаимодействия:\n'
        '1. Добавить контакт\n'
        '2. Вывести на экран\n'
        '3. Поиск контакта\n'
        '4. Выход из программы')

        command = input('Введите номер действия: ')

        while command not in ('1', '2', '3', '4'):
            print('Некорректные данные, нужно ввести число комманды')
            command = input('Введите номер действия: ')

        match command:
            case '1':
                add_contact(create_contact())
            case '2':
                show_info()
            case '3':
                search_contact()
            case '4':
                print('Всего хорошего!')

interface( )