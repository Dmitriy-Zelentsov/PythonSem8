
def get_contact():
    id = input('ID: ')
    first_name = input('Имя: ')
    second_name = input('Фамилия: ')
    position = input('Должность: ')
    salary = input('Зп: ')
    tel = input('Тел: ')
    return (f'{id}|{first_name}|{second_name}|{position}|{salary}|{tel}')

def find_contact(book,serch):
    a = ''
    for line in book:
        if line.find(serch) != -1:
            a += line
    if a  == '':
        return ("Не найдено")
    else:
        return a           

def request():
    return input('Запрос для поиска: ')

def mode():
    return int(input('Для записи,нажать - 1; Для поиска - 2 ; Для изменения - 3; Для выхода - 0: '))


def diff_contact(book):
    index = 0
    line = []
    for_diff = input(('Поиск: '))
    for i in range(len(book)):
        if book[i].find(for_diff)!=-1:
            index = i
    line = book[i].split('|')
    print(line)
    a = int(input('Для смены ID ввести-0; Имени-1; Фамилии-2; Должности-3; ЗП-4; Тел-5: '))
    line [a]= input('Введите новое значение: ')
    delimiter = '|'
    str = delimiter.join(line)
    book[index] = str
    with open('book.txt', 'w',encoding ='utf-8') as f: 
        f.writelines("%s" % place for place in book)
        print('Замена выполнена')
