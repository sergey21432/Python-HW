# задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

print('task_1')
try:
    a = input('Enter a number day of week: ')
    if (float(a) % 1 != 0 or int(a) < 1 or int(a) > 7): print('Entered incorrect data')
    elif (int(a) > 5): print("It's a weekend")
    else: print("It's a weekday")
except: print('Entered incorrect data')

# задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print('\ntask_2')
try:
    a = [True,False]
    for x in a:
        for y in a:
            for z in a:
                print(f'x: {x}, y: {y}, z: {z}, ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z: {not (x or y or z) == (not x and not y and not z)}')
except: print('Entered incorrect data')

# задача 3. Напишите программу, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

print('\ntask_3')
try:
    x= float(input('Enter a value X: '))
    y = float(input('Enter a value Y: '))
    if (x == 0): print("X")
    elif (y == 0): print("Y") 
    elif (x == 0 and y == 0): print("0")
    elif (y > 0):
        if (x > 0): print("1")
        elif (x < 0): print("2")
    elif (y < 0):
        if (x > 0): print("4")
        elif (x < 0): print("3")
except: print('Entered incorrect data')


# задача 4 HARD необязательная Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число, второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") и выводит результат на экран.

# Поддерживаемые операции: +, -, /, *, mod, pow, div, где
# mod — это взятие остатка от деления,
# pow — возведение в степень,
# div — целочисленное деление.

# Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".

# Обратите внимание, что на вход программе приходят вещественные числа.

# Sample Input 1:
# 5.0
# 0.0
# mod
# Sample Output 1:
# Деление на 0!

# Sample Input 2:
# -12.0
# -8.0
# *
# Sample Output 2:
# 96.0

# Sample Input 3:
# 5.0
# 10.0
# /
# Sample Output 3:
# 0.5

print('\ntask_4')
try:
    x = float(input('Enter a value X: '))
    y = float(input('Enter a value Y: '))
    str_operator = input('Enter an operator: ')
    arr_div = ['/', 'mod', 'div']
    if (str_operator == '+'):
        print(x+y)
    elif (str_operator == '-'):
        print(x-y)
    elif (str_operator in arr_div): 
        if  y == 0: print('Деление на 0!') 
        elif str_operator == arr_div[0]: print(round(x/y,1))
        elif str_operator == arr_div[1]: print(round(x%y,1))
        elif str_operator == arr_div[2]: print(round(x//y,1))
    elif (str_operator == '*'):
        print(round(x*y, 1))
    elif (str_operator == 'pow'):
        print(round(x**y, 1))
    else:
        print('Entered incorrect data')
except: print('Entered incorrect data')


# Задача 5 VERY HARD SORT необязательная

# Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.

# Например, задан массив:
# 1 4 7 2
# 5 9 10 3

# После сортировки
# 1 2 3 4
# 5 7 9 10