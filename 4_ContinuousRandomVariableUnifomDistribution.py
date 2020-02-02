print("""
В.Е. Гмурман Руководство к решению задач по теории вероятностей к математической статистике

Создать программу, которая которая обеспечит графический интерфейс визуализации ввода данных и результаты рассчета моделирования случайной величины распределенной равномерно на отрезке А-В

Задание 689 стр. 298

@author: Ilia Gavrilov
""")

import numpy as np 
import matplotlib.pyplot as plt

A = 0 
B = 0

print('Ввод данных')
while True:   
  A = int(input("Введите значение А: ")) 
  B = int(input("Введите значение B: "))
  if A >= B:
    print('A должно быть меньше B')
  elif A < B:
    break

array = np.round(np.random.uniform(A,B,10), 0)
print("Массив непрерывных величин: \n", array)

print('Результаты рассчета представлены на графике')
label = 'Результаты рассчета'
count, bins, ignored = plt.hist(array, 15, density=True)
plt.title(label, fontdict=None, loc='center', pad=None)
plt.show()

plt.savefig('UniformDistribPlot.png')
