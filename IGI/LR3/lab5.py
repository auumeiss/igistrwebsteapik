import random

from lib import int_input


#Задание 5. В соответствии с заданием своего варианта составить программу для обработки вещественных списков.
#Программа должна содержать следующие базовые функции:
#1) ввод элементов списка пользователем;
#2) проверка корректности вводимых данных;
#3) реализация основного задания с выводом результатов;
#4) вывод списка на экран.

#Найти сумму отрицательных элементов списка и произведение элементов, расположенных между максимальным и минимальным элементами

def input_list():
    while True:
        try:
            n = int(input("Введите количество элементов списка: "))
            if n <= 0:
                print("Количество элементов должно быть положительным числом.")
            else:
                break
        except ValueError:
            print("Ошибка: Введите целое число.")

    lst = []
    choose=0
    while choose!=1 and choose!=2:
        print("1.Пользовательский ввод. \n 2. Рандом")
        choose=int_input()
    if choose==1:
        for i in range(n):
            while True:
                try:
                    value = float(input(f"Введите {i+1}-й элемент списка: "))
                    lst.append(value)
                    break
                except ValueError:
                    print("Ошибка: Введите вещественное число.")
    elif choose==2:
        for i in range(n):
            lst.append(random.uniform(-100,100))

    return lst

def sum_negative_elements(lst):
    return sum(x for x in lst if x < 0)

def product_between_max_min(lst):
    if len(lst) < 2:
        return 0

    min_index = lst.index(min(lst))
    max_index = lst.index(max(lst))
    start_index = min(min_index, max_index) + 1
    end_index = max(min_index, max_index)

    product = 1
    for i in range(start_index, end_index):
        product *= lst[i]

    return product

def print_list(lst):
    print("Список:", lst)

def lab5():
    # Ввод списка
    lst = input_list()

    # Вывод списка
    print_list(lst)

    # Находим сумму отрицательных элементов
    sum_negative = sum_negative_elements(lst)
    print("Сумма отрицательных элементов списка:", sum_negative)

    # Находим произведение элементов, расположенных между максимальным и минимальным элементами
    product_between = product_between_max_min(lst)
    print("Произведение элементов, расположенных между максимальным и минимальным элементами:", product_between)
