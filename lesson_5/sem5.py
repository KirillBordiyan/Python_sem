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
    marks = [random.randint(1,5) for _ in range(n)]
    print(marks)
    
    markMax = max(*marks)
    markMin = min(*marks)
    print(markMax, markMin)

    for i in range(len(marks)-1):
        if marks[i] == markMax:
            marks[i] = markMin
        
    print(marks)
    
    
task33()



# from random import randint
# n = 5
# li1 = [randint(1, 5) for i in range(n)]
# print(f'Input: {n} ->', *li1)
# li2 = sorted(li1)

# def merge_two_lists(a, b):
#     c = []
#     i = j = 0
#     while i < len(a) and j < len(b):
#         if a[i] < b[j]:
#             c.append(a[i])
#             i += 1
#         else:
#             c.append(b[j])
#             j += 1
#     if i < len(a):
#         c += a[i:]
#     if j < len(b):
#         c += b[j:]
#     return c


# def merge_sort(li):
#     if len(li) == 1:
#         return li
#     middle = len(li) // 2
#     left = merge_sort(li[:middle])
#     right = merge_sort(li[middle:])
#     return merge_two_lists(left, right)


# for i in range(len(li1)):
#     if li1[i] == li2[len(li1)-1]:
#         li1[i] = li2[0]
# print('Output:', *li1)












# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 


# def task35(n):
#     if n == 1:
#         return False
#     if
    
    
    
    
    





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