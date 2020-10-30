#Дан список любых целых чисел. Исключить из него максимальный элемент/минимальный элемент.

import random
# создаем список случаных 10 элементов 
num = [random.randint(0, 100) for _ in range(10)]
print(num)
a = min(num) # a= max(num)
for i in range(len(num)):
    if num[i] == a:
        num[i] = []
numbers = [elem for elem in num if elem != []]
 
print (numbers)

#Дан список из любых целых чисел, в котором есть два нулевых элемента. Исключить нулевые элементы.

num = [0, 7, 6, 5, 8, 0, 2, 4, 52, 0, 78]
numbers = [elem for elem in num if elem !=0]
 
print (numbers)


#Дан список num, состоящий из целых чисел и целое число b. Исключить из списка элементы, равные b.

import random
num = [random.randint(0, 10) for _ in range(20)]
b = random.randint(0, 10)
print(num)
print(b)
numbers = [elem for elem in num if elem != []]
print (numbers)

#Дан список целых чисел X и числа A1, A2 и A3. Включить эти числа в список, расположив их после второго элемента.

import random
x = [random.randint(0, 10) for _ in range(10)]
A1 = 10
A2 = 9 
A3 = 13
print(x)
x.insert(2, A1)
x.insert(3, A2)
x.insert(4, A3)
print (x)

#Вывести все элементы списка, стоящие до максимального элемента этого списка

import random
# создаем список случаных 10 элементов 
num = [random.randint(0, 100) for _ in range(10)]
print(num)
a = max(num)
print(a)
numbers = []
for i in range(len(num)):
      if num[i] == a:
            num[i] = 0
i = 0
while i < len(num):
    if num[i] !=0:
        numbers.append(num[i])
        i += 1
    else:
        break
      
print(numbers)


#Дан список X и число A. Вычислить сумму всех отрицательных элементов списка Х, значения которых больше, чем A. Подсчитать также количество таких элементов.

X = [-3, 5, -7, -4, -2, 13]
A = -4
q = 0
s = 0
num = [el for el in X if el<0]
for i in range(len(num)):
           if A < num[i]:
                q += 1
                s += num[i]
print(q, s)

#Дан список чисел. Вычислить среднее арифметическое положительных элементов этого списка и среднее арифметическое отрицательных элементов этого списка (0 исключать, он ни положителен, ни отрицателен)

X = [-3, 5, -7, -4, -2, 13, 0]
numn = [el for el in X if el<0]
nump = [el for el in X if el>0]
sn=0
sp=0
for i in range(len(numn)):
                sn += numn[i]
sarn = sn/len(numn)
        
for i in range(len(nump)):
                sp += nump[i]
sarp = sp/len(nump)

print(sn, sarn, sp, sarp)

#Исключить из списка элементы, которые расположенные между максимальным и минимальным значением в этом списке. Можно решить в общем виде. 
#Для тех кому это сложно, можно упростить задачу и брать первый слева минимальный и первый слева максимальный элемент.
