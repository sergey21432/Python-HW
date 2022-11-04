from decimal import Decimal
import random

# # Задача 1. Задайте список из нескольких чисел. Напишите программу, которая
# найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print('task1')


def CheckInt(number):
    try:
        number = float(number)
        if number % 1 == 0 and number > 0:
            return True
        else:
            return False
    except:
        return False


def IntArr(number_val, int_arr):
    int_arr = []
    sum_val = 0
    for i in range(number_val):
        n = random.randint(1, 1000)
        int_arr.append(n)
        if i % 2 != 0:
            sum_val += n
    print(int_arr)
    print(f'Sum odd elements: {sum_val}')
    return int_arr


val_arr = []
while len(val_arr) == 0:
    number = input('Enter an integer positive number more zero: ')
    if CheckInt(number):
        number = int(number)
        val_arr = IntArr(number, val_arr)
    else:
        print('Entered incorrect data')

# Задача 2.  Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

print('\ntask2')


def Mult_Couple(int_arr):
    len_arr = len(int_arr)
    if not (len_arr > 0):
        return None
    arr_mult = []
    for i in range((len_arr + 1) // 2):
        arr_mult.append(int_arr[i] * int_arr[- (i + 1)])
    return arr_mult


print(Mult_Couple(val_arr))

# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая
# найдёт разницу между максимальным и минимальным значением дробной части
# элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print('\ntask3')

lst = [1.1, 1.2, 3.1, 5, 10.01]


def Dif_Frac_Arr(fl_arr):
    len_arr = len(fl_arr)
    if not (len_arr > 0):
        return None
    bln_first = True
    len_max_string = 0
    for i in range(len_arr):
        str_fl = str(fl_arr[i])
        try:
            len_string = len(str_fl[str_fl.index('.') + 1:])
            if len_max_string < len_string:
                len_max_string = len_string
        except:
            len_string = 0
        finally:
            temp_fl = Decimal(fl_arr[i]) - int(fl_arr[i])
            if temp_fl != 0:
                if not bln_first:
                    if temp_fl > max_Frac:
                        max_Frac = temp_fl
                    if temp_fl < min_Frac:
                        min_Frac = temp_fl
                if bln_first:
                    max_Frac = temp_fl
                    min_Frac = temp_fl
                    bln_first = False
    try:
        return round(max_Frac - min_Frac, len_max_string)
    except:
        return None

print (lst)
print(Dif_Frac_Arr(lst))

# Задача 4. Напишите программу, которая будет преобразовывать десятичное
# число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

print('\ntask4')


def Convert_Bin(number_val):
    bin_numb = 0
    count = 0
    while number_val > 0:
        bin_numb += number_val % 2 * (10 ** count)
        number_val //= 2
        count += 1
    return bin_numb


number = input('Enter an integer positive number more zero: ')
if CheckInt(number):
    number = int(number)
    print(Convert_Bin(number))
else:
    print('Entered incorrect data')


# задача5 HARD необязательная.
# Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , причем чтоб 
# количество элементов было четное. Вывести на экран красивенько таблицей. Перемешать случайным образом элементы 
# массива, причем чтобы каждый гарантированно переместился на другое место и выполнить это за m*n / 2 итераций. 
# То есть если массив три на четыре, то надо выполнить не более 6 итераций. И далее в конце опять вывести на экран как таблицу.

print('\ntask5')


def int_tuple(str_val):
    try:
        tuple_val = tuple(map(int, str_val.split()))
        mult = tuple_val[0] * tuple_val[1]
        if mult == 0: return None
        if mult % 2 != 0: return None
        if len(tuple_val) == 2: return tuple_val
        else: return None
    except: return None


def arr_float(tuple_val):
    try:
        arr_val = []
        for _ in range(tuple_val[0]):
            list_val = []
            for _ in range(tuple_val[1]):
                list_val.append(round(random.uniform(-1000, 1000),2))
            arr_val.append(list_val)   
        return arr_val
    except: return None


def shuffle_arr(arr_val):
    try:
        dict_ind = {}
        len_arr_1 = len(arr_val)
        len_arr_2 = len(arr_val[0])
        int_iteration = (len_arr_1 + 1) // 2 * len_arr_2
        if len_arr_1 % 2 != 0: 
            int_iteration -= len_arr_2 // 2
        for _ in range(int_iteration):
            while True:
                indx_1_1 = random.randint(0, len_arr_1 - 1)
                indx_1_2 = random.randint(0, len_arr_2 - 1)
                str_indx_1 = str(indx_1_1) + '_' + str(indx_1_2)
                if not (str_indx_1 in dict_ind.keys()): break
            while True:
                indx_2_1 = random.randint(0, len_arr_1 - 1)
                indx_2_2 = random.randint(0, len_arr_2 - 1)
                str_indx_2 = str(indx_2_1) + '_' + str(indx_2_2)
                if not (str_indx_2 in dict_ind.keys()) and str_indx_1 != str_indx_2: break

            temp_numb = arr_val[indx_1_1][indx_1_2]
            arr_val[indx_1_1][indx_1_2] = arr_val[indx_2_1][indx_2_2]
            arr_val[indx_2_1][indx_2_2] = temp_numb
            dict_ind[str_indx_1] = None
            dict_ind[str_indx_2] = None
        print(f'Iteration: {int_iteration}')
        return

    except:
        return None


def print_arr(arr_val):
    max_len = 0
    for elem in arr_val:
        for val in elem:
            if max_len < len(str(val)): max_len = len(str(val))

    for elem in arr_val:
        for val in elem:
            print(str(val) + (max_len - len(str(val))) * ' ', end='   ')
        print('')


tuple_value = int_tuple(input('Enter size of demension of array like two positive integer numbers separated by a whitespace: '))

if tuple_value is None: print('Incorrect data')
else:
    arr_val = arr_float(tuple_value)
    print_arr(arr_val)
    print('\n')
    shuffle_arr(arr_val)
    print_arr(arr_val)


