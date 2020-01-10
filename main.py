"""
Create a program that displays the values of random variables (random numbers), which are distributed according to the normal / uniform distribution

Создать программу, которая выводит значения случайных величин (числа random), которые распределяются по нормальному/равномерному распределению

@author: Ilia Gavrilov
"""

# libraries import
# импорт библиотек
import numpy as np 
import matplotlib.pyplot as plt 

# mean and standard deviation
# среднее и стандартное отклонение
mean = 0 
std = 0.1

# 1D Array as per Gaussian Distribution
# Одномерный массив в соответствии с распределением Гаусса 
array = np.random.normal(0, 0.1, 1000) 
print("1D Array filled with random values "
      "as per gaussian distribution : \n", array); 

# Plotting
# Построение диаграммы распределения
count, bins, ignored = plt.hist(array, 30, density=True) 
plt.plot(bins, 1/(std * np.sqrt(2 * np.pi)) *
          np.exp( - (bins - mean)**2 / (2 * std**2) ), 
          linewidth=2, color='r') 
plt.show() 

plt.savefig('NornalDistribPlot.png')