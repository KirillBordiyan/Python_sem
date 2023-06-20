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
    
    if a < 0:
        return -1
    elif a == 0:
        return "1"
    elif a == 1:
        return "2 and 3"
    
    while temp <= a:
        temp = f0 + f1
        f0 = f1
        f1 = temp
        count += 1
        if temp == a:
            return count
    else:
        return "not include feb"

        
# print(task11())
        
    
# Задача №13.
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2
    
def task13():
    n = int(input("need: "))
    if n > 100:
        n = int(input("input less than 100: "))
    
    temper = []
    while len(temper) < n:
        addTemp = int(input(f"input {len(temper)+1} day temperature: "))
        if addTemp not in range(-50, 51):
            addTemp = int(input("this can't be: "))
        temper.append(addTemp)

    startWarmPeriod = 0
    warmPeriod = 0
    for currentTemperature in temper:
        if currentTemperature > 0:
            startWarmPeriod += 1
            if warmPeriod < startWarmPeriod:
                warmPeriod = startWarmPeriod
        else:
            startWarmPeriod = 0
                        
    return warmPeriod
    
# print(task13())


def task13var2():

    days = int(input("need: "))
    if days > 100:
        days = int(input("input less than 100: "))
    
    
    startWarmPeriod = 0
    warmPeriod = 0
    i = 0
    for i in range(0,days):
        averageDayTemp = int(input(f"input {i+1} day temperature: "))
        if averageDayTemp not in range(-50, 51):
                averageDayTemp = int(input("this can't be: "))
                
        if averageDayTemp > 0:
            startWarmPeriod +=1
            if warmPeriod < startWarmPeriod:
                    warmPeriod = startWarmPeriod
        else:
            startWarmPeriod = 0
            
        i += 1
        
    return warmPeriod


print(task13var2())









# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

def task15():
    n = int(input("watermelons: "))
    if n <= 0:
        n = int(input("input real number watermelons: "))
        
    
