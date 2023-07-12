import datetime
# все, что вводит польхователь
def input_num():
    ask = int(input("выберите действие:\n1 - записать нового ползователя\n2 - Найти пользователя \n3 - Изменить пользователя \n4 - Удалить пользовтаеля\n5 - Выход \n"))
    return ask

def input_id(args):
    id = input(args)
    return id

def input_name(args):
    name = input(args)
    return name

def input_date_birth(args):
    birth = input(args)
    if birth == "\n":
        birth = datetime.datetime.now()
    return birth

def input_tel(args):
    tel = input(args)
    return tel

def search_par():
    par = int(input("1 по id\n2 по имени\n3 по дате\n4 по телефону\n"))-1
    return par













# def input_num():
#     ask = int(input("Выберите действие: \n 1 - Записать данные нового пользователя \n 2 - Переименовать пользователя \n 3 - Удалить пользователя \n 4 - Найти пользователя \n 5 - Переместить пользовтаеля в другую группу \n 6 - Выход \n"))
#     return ask
# def input_name():
#     a = input("Введите id - ")
#     a1 = input("Введите ФИО - ")
#     a2 = input("Введите дату рождения - ")
#     a3 = (f" {a} , {a1} , {a2}\n")
#     return a3

# def input_search():
#     s = input("Введите характеристику - ")
#     return s

# # id, ФИО, дата рождения
# # 1) Ввод нового пользователя
# # 2) Поиск по определенной характеристике -> ввод хар-ки
# # предлагаем на выбор строчки подходящие, пользователем, он выбирает и мы изменяем