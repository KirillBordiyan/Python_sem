from view import * 
# вся запись в файл из вводимых данных
def write_all(id, name, birth, tel):
    with open('lesson_8/tel.txt', 'a', encoding='UTF-8') as file:
        file.write(f"{id}, {name}, {birth}, {tel} \n")


def search_data(par, search_name):
    with open('lesson_8/tel.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            if search_name in line.split(',')[par]:
                print(line)
                

def show_all():
    with open('lesson_8/tel.txt', 'r', encoding='UTF-8') as file:
        print(file.read())
    
    
def change(id):
    with open('lesson_8/tel.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            if id == line.split(',')[0]:
                print(line)
                data = line.split(',')
    with open('lesson_8/tel.txt', 'w', encoding='UTF-8') as file:            
        confirm_change = int(input("1- меняем\n0- нет"))
        if confirm_change == 0:
            pass
        if confirm_change == 1:
            change = int(input("что меняем?\n1-id\n2-Имя\n3-дату\n4-телефон\n"))
            match change:
                case 1:
                    input_id("новый id: ")
                case 2:
                    input_name("новое имя: ")
                case 3:
                    input_date_birth("новая дата: ")
    
        



# def search_name(name):
#     with open("telephone.txt", "r", encoding="UTF-8") as file:
#         a = file.readlines()
#         for line in a:
#             if name in line: 
#                 print(line)