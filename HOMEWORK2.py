
# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11
print('task1')
try:
    number = abs(float(input('Enter a number: ')))
    while (round(number%1,10)!=0):
        number *=10
    sum_digit = 0
    int_number = int(number)
    while (int_number//1 > 0):
        sum_digit += int_number % 10
        int_number //=10
    print(sum_digit)
except: print('Entered incorrect data')

# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
print('\ntask2')
try:
    number = float(input('Enter an integer positive number more zero: '))
    if number%1 == 0 and number > 0:
        number = int(number)
        mult = 1
        arr_res = []
        for i in range(1, number+1):
            mult *= i
            arr_res.append(mult)
        print(arr_res)
    else: print('Entered incorrect data')
except: print('Entered incorrect data')

# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
print('\ntask3')
sp = input('Введите искомую фразу: ')
sp_in = input('Введите фразу для поиска: ')

int_count = 0
int_len_sp = len(sp)
if sp in sp_in:
    for i in range(len(sp_in)):
        if sp[0] == sp_in[i]:
            if sp_in[i:i + int_len_sp] == sp:
                int_count +=1
                i = i + int_len_sp
print(int_count)

# Задача 4 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу, которая принимает на вход N, и координаты двух точек и находит расстояние между ними в N-мерном 
# пространстве.

print('\ntask4')
try:
    number = float(input('Enter dimension of space as an integer positive number more zero: '))
    if number%1 == 0 and number > 0:
        number = int(number)
        sum_delta = 0
        for i in range(number):
            sum_delta += (float(input('Enter coordinate first point: ')) - float(input('Enter coordinate second point: ')))**2
        print(round(sum_delta ** 0.5,3))
    else: print('Entered incorrect data')
except: print('Entered incorrect data')

# Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z . Но теперь количество предикатов 
# не три, а генерируется случайным образом от 5 до 25, сами значения предикатов случайные, проверяем это утверждение 100 раз, с помощью модуля time 
# выводим на экран , сколько времени отработала программа.




