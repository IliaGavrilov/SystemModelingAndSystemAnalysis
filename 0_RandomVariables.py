"""
Создать программу, которая выводит значения случайных величин (числа random)

@author: Ilia Gavrilov
"""

# импорт библиотеки
import random

# Объявление массива и запуск цикла для генерирования случайных чисел
X = []
for i in range(0, 100):
  X.append(round(random.random(), 2))

print("Массив случайных величин: \n", X); 