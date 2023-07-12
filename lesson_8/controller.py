from database import *
from view import *
# общая менюшка пользователя

def main():
    while True:
        num = input_num()
        
        match num:
            case 1:
                id = input_id("id: ")
                name = input_name("Имя пользователя: ")
                date = input_date_birth("добавить дату ДД.ММ.ГГГГ: ")
                tel = input_tel("добавить телефон")
                write_all(id, name, date, tel)
                print("записано")
            case 2:
                par = search_par()
                search_name = input_name(f"Поиск по параметру {par+1}: ")
                search_data(par, search_name)
            case 3: 
                show_all()
                id = input_id("id для замены: ")
                change(id)
            # case 4:
            case 5:
                return False
        
        

main()












# from database import*
# from view import*

# def main():
#     while True:
#         num = input_num()
#         match num:
#             case 1:
#                 name = input_name()
#                 write_name(name)
#                 print("Успешно записано \n")
#             case 2:
#                 s = input_search()
#                 search_name(s)
#                 print("Успешно найдено \n")
#             case 3:
#                 name = input_name()
#                 write_name(name)
#                 print("Успешно удалено \n")
#             case 4:
#                 name = input_name()
#                 write_name(name)
#                 print("Успешно найдено \n")
#             case 5:
#                 name = input_name()
#                 write_name(name)
#                 print("Успешно переместил \n")
#             case 6:
#                 print("Выход")
#                 return()

# main()