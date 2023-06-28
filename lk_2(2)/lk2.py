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
col.add('white')
col.remove('white')
print(col)
col.clear()
print(col)

# a = {1,2,3,4,5,6,7,8,9}
# b = {3,5,7,9,14}
# c = a.copy
# print(c)
# u = a.union(b)
# print(u) #объединяет множества, но значения всегда уникальны (при совпадении не добавляются)
# i = a.intersection(b) #пересечение
# print(i)
# d1 = a.difference(b)#чего нет в а, что есть в b
# d2 = b.difference(a)#чего нет в b, что есть в а
# print(d1)
# print(d2)

