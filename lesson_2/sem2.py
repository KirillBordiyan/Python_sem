# 9. По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120


def task9():
    n = int(input())
    f = 1
    i = 1
    if n == 0:
        return f
    elif n < 0:
        return -f
    else:
        while i <= n:
            f *= i
            i+=1
        return f
        
# print(task9())


# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# начинаем 0 1, а дальше счет
def task11():
    
    f0 = 0
    f1 = 1
    temp = 0
    count = 2
    
    a = int(input())
    
    if a <= 0:
        return -1
    elif a == 0 or a == 1:
        return f"{a+1} and 3"
    
    while temp <= a:
        temp = f0 + f1
        f0 = f1
        f1 = temp
        count += 1
        if temp == a:
            return count
    else:
        return "not include fed"

        
# print(task11())
        
    
    
    