# def calc1(a, b):
#     return a + b

# calc1 = lambda a,b: a +b


# def calc2(a, b):
#     return a * b

# def math(f, x, y):
#     print(f(x,y))
    
# math(calc1, 4,5) # == math(lambda a,b: a + b, 4 ,9)


#------------------------------------------------------------------------------------------------------
# array = [1,2.2,3,5,8.9,10]
# new = []
# for i in array:
#     if i % 2 == 0:
#         new.append(i, i**2)

# # print(new)


# def select(func, num):
#     return [func(x) for x in num] #вовар список, где к каждому элементу применяется func

# def where(func, num):
#     return [x for x in num if func(x)] #возвр только те значения, которые прошли проверку func(x) 

# result = select(int, array) # данные приводятся в вид, который нам нужен
# print(result)
# result = where(lambda x: x % 2 == 0, result) #вместо переменной func исп lambda для списка result
# print(result)

# result = select(lambda x: (x, x**2), result)# список будет обновлен,  применяем lambda-f для каждого элемента
#                                         #чтобы на выходе (..: ->) получить кортеж (x, x**2) из списка result 
# print(result)
#------------------------------------------------------------------------------------------------------



# map - принимает 2 арг: функция и объект
# функция применяется ко всем элементам переданного объекта и возвращает новый объект

# list1 = [i for i in range(1,21)]
# print(list1)

# list1 = list(map(lambda i: i + 10, list1)) #передаем lambda-функцию к списку list1 и возвращаем его
# print(list1)

#------------------------------------------------------------------------------------------------------


# с клавиатуры вводится набор чисел через пробел
# перевести list-строк в list-чисел

#мое
# array = ['1','2','3']
# print(array, type(array[0]))
# array = list(map(int, array))
# print(array, type(array[0]))


# data = '1 4 56 78 2 27 86' #строка
# # data.split() #список str разделенных пробелами
# data = list(map(int, data.split()))
# print(data)

#------------------------------------------------------------------------------------------------------


#filter - фильтрация значений
# 2 аргумента: функция и объект 
# возврат только тех элементов объекта, для которых значение функции True

# array = [15,2,5,68,98,345,2342]

# result = list(filter(lambda i: i % 10 == 5, array))
# print(result)
#------------------------------------------------------------------------------------------------------

#zip - применяется к набору итерируемых объектов
# возвращает итератор с кортежами из элементов вхожных данных
# если передается несколько списков разной длинны, итерироваться будет по минимальному из них



#------------------------------------------------------------------------------------------------------
#enumerate() - применяется к итерироемому объекту и возвращает новый итератор с кортежами из индекса и 
# элементов входящих данных
# как бы нумерует входящие данные

#------------------------------------------------------------------------------------------------------

#                                                   ФАЙЛЫ
# в текстовом формате используются для:
#     хранения
#     передачи в клиент-серверных проектах
#     хранени конфигов
#     логирования действий
    
# что нужно для работы с ними: 
#     завести переменную, которая будет связана с текстовым файлом 
#     указать путь к нему
#     указать режим работы с файлом


# режимы работы с файлами:
#     а (ab) - открытие для добавления данных:
#         -позволяет дописывать что-то в имеющийся файл
#         -если файла до этого нет - он создатся и в него начнется запись
    
#     r - открытие для чтения:
#         -позволяет читать данные файла
#         -если начать читать из несуществующего файла, программа выдаст ошибку
    
#     w - открытие для записи данных:
#         -позволяет записать данные и создать файл, если его не существует
#         -данные ПЕРЕЗАПИСЫВАЮТСЯ
    
#     w+      : миксовый
#         - позволяет открыть для записи и читать из него
#         - если файла нет - он его создаст
        
#     r+       : миксовый
#         -открывает для чтения и записи в него
#         -если файла нет, выдаст ошибку 
    
    

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.close()

# with open('file.txt', 'w') as data:
#     data.write('line 1 \n')
#     data.write('line 3 \n')

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()


#------------------------------------------------------------------------------------------------------


# работа с оперционной системой
# Модуль OS 
# это множество функций для работы с ОС, которые не зависят от типа ОС, что делает их переносимыми

# чтобы начать работать с данным можулем, его необходимо импортировать:
#     import os
    
# базовые функции:
#     os.chdir(path) - смена текущей директории
    
#     os.getcwd() - текущая рабочая директория
    
#     os.path - вложенный модуль в os и исп для работы с путями:
    #     os.path.basename(path) - базовое имя пути (получим имя файла)
    #     os.path.abspath(path) - возвращает нормализованный абсолютный путь (получим путь к файлу по имени)
    
    
    
# модуль shutil
# исп для обработки файлов, групп файлов, папок. 
# функции позволяют копировать, добавлять, удалять файлы и папки

# import shutil

# shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) src в dst
# shutil.copy(src,dst) - копирует содержимое src в файл или папку dst
# shutil.rmtree(path) - удаляет директорию и все поддериктории; path должен указывать на директорию,
#                         а не на символическую ссылку