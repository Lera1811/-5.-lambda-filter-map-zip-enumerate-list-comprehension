# Дан список случайных чисел. Создайте список, 
 # в который попадают числа, описывающие возрастающую последовательность. 
 # Порядок элементов менять нельзя.
 # [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
 
 
 import random

numbers = [random.randint(1,15) for i in range(15)]
 print(numbers)
 list = [0]
 list[0] = numbers[0]

 for i in range(len(numbers)):
     if numbers[i] > list[-1]:
         list.append(numbers[i])

 print(list)