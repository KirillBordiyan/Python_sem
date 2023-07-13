import datetime

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
