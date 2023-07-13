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
    with open('lesson_8/tel.txt', 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        lines.sort(key = lambda line: int(line.split(',')[0].strip()))
    with open('lesson_8/tel.txt', 'w', encoding='UTF-8') as file:
        for line in lines:
            file.write(line)
        
def delete_data(search_data): 
    with open('lesson_8/tel.txt', 'r', encoding='UTF-8') as file:
        lines = file.readlines()
    with open('lesson_8/tel.txt', 'w', encoding='UTF-8') as file:
        for line in lines:
            if search_data != line.strip().split(',')[0]:
                file.write(line)
                