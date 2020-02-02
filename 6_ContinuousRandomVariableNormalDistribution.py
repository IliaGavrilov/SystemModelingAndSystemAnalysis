print("""
В.Е. Гмурман Руководство к решению задач по теории вероятностей к математической статистике

Создать программу, которая выводит значения случайных величин (числа random), которые распределяются по нормальному/равномерному распределению

Задание 710 стр. 302

@author: Ilia Gavrilov
""")
# импорт библиотек
import numpy as np 
import matplotlib.pyplot as plt 

# среднее и стандартное отклонение
mean = 0 
std = 0.1

# Одномерный массив в соответствии с распределением Гаусса 
array = np.random.normal(0, 0.1, 1000) 
print("Массив случайных величин по нормальному распределению: \n", array[:15]); 
print('Результаты рассчета представлены на графике NornalDistribPlot.png')

# Построение диаграммы распределения
count, bins, ignored = plt.hist(array, 30, density=True) 

# Отрисовка кривой пиковых значений
plt.plot(bins, 1/(std * np.sqrt(2 * np.pi)) *
          np.exp( - (bins - mean)**2 / (2 * std**2) ), 
          linewidth=2, color='r') 
label = 'Распределение случайных величин по нормальному закону'
plt.title(label, fontdict=None, loc='center', pad=None)
plt.show() 

plt.savefig('NornalDistribPlot.png')
