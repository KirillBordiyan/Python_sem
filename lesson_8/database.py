from view import * 
# вся запись в файл из вводимых данных
def write_all(id, name, birth, tel, par = 'a'):
    with open('lesson_8/tel.txt', par, encoding='UTF-8') as file:
        file.write(f"{id}, {name}, {birth}, {tel} \n")


def search_data(par, search_name):
    with open('lesson_8/tel.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            if search_name in line.split(',')[par]:
                print(line)
                

def show_all():
    with open('lesson_8/tel.txt', 'r', encoding='UTF-8') as file:
        print(file.read())
    
    
def change_data(id, new_name, new_date, new_tel):
    with open('lesson_8/tel.txt', 'r', encoding='UTF-8') as file:
        lines = file.readlines()  #["1,rr,111", "2,tt,222"]
    with open('lesson_8/tel.txt', 'w', encoding='UTF-8') as file:
        for line in lines:
            if id != line.strip().split(',')[0]:
                file.write(line)
    write_all(id, new_name, new_date, new_tel)

def sort():
    pass
#     with open('lesson_8/tel.txt', 'r+', encoding='UTF-8') as file:
#         for line in file.readlines():
#             line.split(',').sort(key= lambda line: int(line[0]))
        
    
                
def delete_data(search_data): 
    with open('lesson_8/tel.txt', 'r', encoding='UTF-8') as file:
        lines = file.readlines()
    with open('lesson_8/tel.txt', 'w', encoding='UTF-8') as file:
        for line in lines:
            if search_data != line.strip().split(',')[0]:
                file.write(line)
                
                
                
                
                
#     # with open('lesson_8/tel.txt', 'w', encoding='UTF-8') as file2:           
    #     confirm_change = int(input("1- меняем\n0- нет"))
    #     if confirm_change == 0:
    #         pass
    #     if confirm_change == 1:
    #         change = int(input("что меняем?\n1-id\n2-Имя\n3-дату\n4-телефон\n"))
    #         match change:
    #             case 1:
    #                 data[0] = input_id("новый id: ")
    #             case 2:
    #                 data[1] = input_name("новое имя: ")
    #             case 3:
    #                 data[2] = input_date_birth("новая дата: ")
    #             case 4:
    #                 data[3] = input_tel("новый телефон: ")
        
        



# def search_name(name):
#     with open("telephone.txt", "r", encoding="UTF-8") as file:
#         a = file.readlines()
#         for line in a:
#             if name in line: 
#                 print(line)