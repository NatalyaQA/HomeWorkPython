"""4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
     периметр квадрата, площадь квадрата и диагональ квадрата.
"""
line = "_________________________________________\n"
task = "Задание №"
num = 1
# line2 = f'{line} {task} {num}'

print(task + "1")
import math as m

def square(side):
    return (side * 4, side**2, round(m.sqrt(2 * (side**2)), 2))

print(square(4))

print(line + task + "2")
"""4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно 
     в формате аргумент: значение. Например:
	name: John
	last_name: Smith
	age: 35 
	position: web developer
"""
def name_arg(**kwargs):
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))

name_arg(name='Лев', last_name='Толстой', age=85, possition='писатель', book='Воина и мир')
print(line + task + "3")
# 4.3 Используя лямбда-выражение, из списка my_list создайте новый список, содержащий только положительные числа
my_list = [20, -3, 15, 2, -1, -21]
func = list(filter(lambda x: x >= 0, my_list))
print(func)

print(line + task + "4")
# 4.4 Используя лямбда-выражение, получите результат перемножения значений в предыдущем списке
my_list = [20, -3, 15, 2, -1, -21]
from functools import reduce
#res = reduce(lambda x, y: x * y, my_list)
res = reduce(lambda x, y: x * y, func)
print(res)

print(line + task + "5")
# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
from HW4_my_calc import *

print(cubing(3))
print(sum_it(99, 3))
print(prod(99, 3))
print(diff(99, 3))
print(devision(99, 3))
print(squaring(6))

