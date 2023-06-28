from modul import max1 as qwqw
# import modul as m1 - вызов модля через новое имя
# import modul * - все методы из файла модуль
# import modul - импорт всех методов, но к ним надо обращаться через modul.xxx
def sumNumbers(y = "Hello"):
    sum = 0
    print(y)
    n = int(input())
    for i in range(n+1):
        sum += i
    return sum
# print(sumNumbers("bye"))



def sum_str(*args): #принимает заранее неизвестное кол-во аргументов
    res = ""
    for i in args:
        res += i
    return res

# print(sum_str("q","w","e"))

# print(qwqw(5,9))

def Febb(n):
    if n in [1,2]:
        return 1
    return Febb(n-1)+Febb(n-2)

    
list1 = [0]
for i in range(1,10):
    list1.append(Febb(i))
    
# print(list1)

    
    
    
#алгоритмы сортировки

# быстрая - что-то типа бинарного поиска, все, что больше - в одну сторону, что меньше - вдругую
# для новых списков повторяем, пока не наткнемся на базовый случай

def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        priv = array[0]
    less = [i for i in array[1:] if i <= priv]
    great = [i for i in array[1:] if i >= priv]
    
    return quickSort(less) + [priv] + quickSort(great)


# print(quickSort([14,5,9,45,2,436,23,76,98,34]))



# сортировка слиянием

def mergeSort(nums):
    if len(nums) > 1:
        mid = len(nums)//2
        left = nums[:mid]
        right = nums[mid:]
        mergeSort(left)
        mergeSort(right)
        i = j = k = 0 
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1                        
                
                
list2 = [1,23,68,678,34,234,98,56,345,234]

mergeSort(list2)
print(list2)