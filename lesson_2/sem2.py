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
    else:
        while i <= n:
            f = f * i
            i+=1
        return f
        
print(task9())


