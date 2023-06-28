# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2


def CharCounter(stroka):
    arrayOfChar = stroka.split() #['a', 'a', 'a', 'b', 'c', 'a', 'a', 'd', 'c', 'd', 'd']
    print(arrayOfChar)
    
    result = {}
    
    for i in arrayOfChar:
        if i in result:
            result[i] += 1
            print(f"{i}_{result[i]}", end = " ")
        else:
            result[i] = 0
            print(i,end =" ")
        
    
CharCounter('a a a b c a a d c d d')



# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.

# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


def task27(args):
    new = args.lower().split()
    result = {}
    
    for i in new:
        if i in result:
            continue
        else:
            result[i] = 0
    print(len(result))

def task27_2(args):
    print(len(set(args.lower().split())))



args = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
task27(args)
task27_2(args)




# 29  “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”

def task29():
    n = int(input())
    maxNum = n
    while n != 0:
        n = int(input())
        if n > maxNum:
            maxNum = n
    print(maxNum)
    
task29()
