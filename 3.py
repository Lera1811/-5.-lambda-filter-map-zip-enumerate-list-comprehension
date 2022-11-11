 #Задайте список случайных чисел от 1 до 10. 
 # Посчитайте, сколько всего совпадающих элементов есть в списке. 
 # Удалите все повторяющиеся элементы.
 # [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают 
 # Список уникальных элементов
 # [1, 4, 2, 3, 6, 7]

 import random

 numbers = [random.randint(1,10) for i in range(10)]

 ListBeforeSet = []
 ListAfterSet = []
 count = 0
 countAnswer = 0
 ListBeforeSet.extend(numbers)
 numbers = set(numbers)
 numbers = list(numbers)
 ListAfterSet.extend(numbers)

 ListAnsver = []

 for i in range(len(ListBeforeSet)):
     for n in  range(len(ListAfterSet)):
         if ListBeforeSet[i] == ListAfterSet[n]:
             ListAnsver.append(ListBeforeSet[i])
             ListAfterSet[n] = -999

 for n in range(len(ListAnsver)):
     for i in  range(len(ListBeforeSet)):
         if ListAnsver[n] == ListBeforeSet[i]:
             count += 1
     if count > 1:
         countAnswer = countAnswer + count
     count = 0
