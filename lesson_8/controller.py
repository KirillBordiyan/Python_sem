from database import *
from view import *

def main():
    while True:
        num = input_num()
        
        match num:
            case 1:
                id = input_id("id: ")
                name = input_name("Имя пользователя: ")
                date = input_date_birth("добавить дату ДД.ММ.ГГГГ: ")
                tel = input_tel("добавить телефон: ")
                write_all(id, name, date, tel)
                print("записано")
            case 2:
                par = search_par()
                search_name = input_name(f"Поиск по параметру {par+1}: ")
                search_data(par, search_name)
            case 3: 
                show_all()
                id = input_id("id для замены: ")
                new_name = input_name("Заменить имя пользователя: ")
                new_date = input_date_birth("обновить дату ДД.ММ.ГГГГ: ")
                new_tel = input_tel("обновить телефон: ")
                change_data(id, new_name, new_date, new_tel)
                sort()
                show_all()
            case 4:
                show_all()
                delete_id = input_id("id для удаления: ")
                delete_data(delete_id)
            case 5:
                return False
        
main()
