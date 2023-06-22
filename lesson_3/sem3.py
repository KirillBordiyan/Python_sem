# dct = {i:1 for i in range(0,150)}



#  №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

def task17():
    numbers = [1, 1, 2, 0, -1, 3, 4, 4]
    
    print(len(set(numbers)))

        
# task17()

def task172():
    numbers = [1, 1, 2, 0, -1, 3, 4, 4, 4, 6]
    
    for i in numbers:
        if numbers.count(i) > 1:
            for j in range(numbers.count(i)-1):
                numbers.remove(i)
                
    print(len(numbers))
    
# task172()
    
            

# №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]


def task19():
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = int(input())
    
    for i in range(k):
            numbers.insert(0,numbers.pop())
            
    print(numbers)
        
# task19()



def task192():
    k = 2
    a = [1, 2, 3, 4, 5]
    memory = 0
    for _ in range(k):
        memory = a[-1]
        a.pop()
        a.insert(0, memory)
    print(a)
    
# task192()




# №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


def task21():
    lst = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
            {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
    
    a = set()
    for i in lst:
        a.add(str(*i.values()).strip())
        
    
    return a

# print(task21())



# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)



def task23():
    list1 = [0, -1, 5, 2, 3]
    count = 0
    for i in range(len(list1)):
        if list1[i] > list1[i-1]:
            count += 1
            
    print(count)
    
# task23()