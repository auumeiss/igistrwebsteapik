import math
from lib import int_input, float_input


# Задание 1. В соответствии с заданием своего варианта составить программу для вычисления
# значения функции c помощью разложения функции
# в степенной ряд. Задать точность вычислений eps.

# ln((x+1)/(x-1))=2(1/x+1/3x^3+1/5x^5+...), |X|>1
def lab1():
    x = 1
    while abs(x) <= 1:
        print("Input x which more than 1 or less than -1")
        x = int_input()
    eps = 0
    while eps <= 0 or eps >= 1:
        print("Input 0<eps<1")
        eps = float_input()

    result = ln_function(x, eps, 500)
    math_result = math.log((x + 1) / (x - 1))

    print(f"Значение функции ln((x+1)/(x-1)) при x = {x}:")
    print(f"{result / 2}")
    print(f"С помощью разложения в ряд: {result}")
    print(f"С помощью модуля math: {math_result}")


# Вычисление суммы
def ln_function(x, eps, max_iterations):
    result = 0.0
    n = 1
    term = (1 / x)

    while abs(term) > eps and n <= max_iterations:
        result += term
        n += 2
        term = 1 / (n * (x ** n))

    if n > max_iterations:
        print("Достигнуто максимальное количество итераций")
    else:
        print("Количество членов ряда, необходимых для достижения указанной точности:", n // 2-1)

    return result * 2
