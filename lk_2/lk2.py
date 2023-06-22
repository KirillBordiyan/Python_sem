list1 = []
list2 = list()
# создание списков, изменяемые


list1.append(1)
print(list1)


for i in range(0,5):
    list1.append(i)
    print(list1)
    

print(list1.pop(2))


t = () #кортеж 
t = (1,2,3)
print(type(t))
# кортежи -неизменяемы

a,b,c = t

print(t)


d = {} #словарь, ключ-значение
d = dict()

d['q'] = "5678" #создание ключ-значение
print(d) #{'q': '5678'}
d['w'] = "9090"
print(d)
del d['q'] #удаление ключ-значения по ключу
for item in d:
    print('{}: {}'.format(item, d[item]))
    
for (key, value) in d.items():
    print(key, value)


# d.items() - кортеж с ключей-значений



# множества - элементы не могут повторяться 
col = set()
col = {'red', 'blue', 'green', 'black'}
print(col)
col.add('white')
print(col)
col.remove('white')
print(col)
col.clear()
print(col)

a = {1,2,3,4,5,6,7,8,9}
b = {3,5,7,9,14}
c = a.copy
print(c)
u = a.union(b)
print(u) #объединяет множества, но значения всегда уникальны (при совпадении не добавляются)
i = a.intersection(b) #пересечение
print(i)
d1 = a.difference(b)#чего нет в а, что есть в b
d2 = b.difference(a)#чего нет в b, что есть в а, вычитаем из б а
print(d1)
print(d2)
n = frozenset(a)#делаем множество неизменяемым




#генератор списков
list_1 = [exp for exp in range(0,5)] #добавляем i в множество, где i в range(0,5) 
print(list_1)#1,2,3,4


list_2 = [i for i in range(0,20) if i % 2 == 1]#добавляем i, которые подходят по условию нечетности
print(list_2)


list_3 = [(i,i) for i in range(0,20) if i % 2 == 1]#добавляем кортеж из i, которые подходят по условию нечетности
print(list_3)


# основные ошибки
# синтаксические  - :
# отступы
# типвые, строка+число и пр
# деление на 0
# ошибка ключа, его отсутствие
# ошибка имени переменной - n & m, name & names
# ошибка значения, приведение типов str -> int 