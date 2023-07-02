import random
# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7 ???? 0 1 1 2 3 5 8 13 21 ????
# Output: 21 ????




# n = int(input("N-е число: "))

def task31(n):
    if n in (1,2):
        return 1
    else:
        return task31(n-2)+task31(n-1)

# print(task31(n))



# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1



def task33():
    n = int(input("N-оценок в журнале: "))
    marks = [random.randint(1,5) for _ in range(n)] #[2, 4, 3, 1, 1, 4, 5, 2, 4, 3]
    print(marks)
    
    markMax = max(*marks)
    markMin = min(*marks)
    print(markMax, markMin)

    for i in range(len(marks)-1):
        if marks[i] == markMax:
            marks[i] = markMin
        
    print(marks)                                    #[2, 4, 3, 1, 1, 4, 1, 2, 4, 3]
    
    
# task33()






# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 


def task35(n, delit = 2):
    if n == 1:
        return False
    if n == delit:
        return True
    else:
        if n % delit != 0:
            delit += 1
            return task35(n, delit)
        return False
        
print(task35(int(input("N: ")))) 
    
    
    
    
    





# Задача №37. Решение в группах
# 15 минут
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3


# from random import randint
# n = 5
# li1 = [randint(1, 5) for i in range(n)]
# print(f'Input: {n} ->', *li1)
# li2 = li1[::-1]
# print(*li2)


# D = input()

# print(D[::-1])