print('''
А.В. Иванов, А.П. Иванова Моделирование случайных величин, систем массового обслуживания и случайных процессов

Лабораторная работа No 1. стр. 13-17

Задан закон распределения дискретной случайной величины X. Нужно выполнить ряд заданий.

@author: Илья Гаврилов, гр. 9093з
''')

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import random

print('Вариант 19:')
X = np.array([-11,-1,1], dtype=float)
print('X =', X)
p = np.array([0.3, 0.6, 0.1], dtype=float)
print('p =', p)
N = 110
print('N =', N)
q = 16
print('q =', q, '\n')

print('1. Смоделировать на ПЭВМ N значений случайной величины методом обратной функции. \n')
print('Поcтроим многоугольник распределения (см. DiscreteVariablesPolygonDistribution.png). \n')
plt.plot(X, p, color='blue', marker='^', linestyle='dashed', linewidth=2, markersize=12)
for x,y in zip(X,p):
    label = "{:.2f}".format(y)
    plt.annotate(label,
                 (x,y),
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center')
label = 'Многоугольник распределения'
plt.title(label, fontdict=None, loc='center', pad=None)
plt.savefig('DiscreteVariablesPolygonDistribution.png')

print('Построим функцию распределения F(x) = P(X < x).')
tempX = np.append(np.NINF, X)
tempX = np.append(tempX, np.Infinity)
#print(tempX)

tempP = np.append(0, p)
tempP = np.append(tempP, 0)
#print(tempP)

# Пары значений для таблицы
pairs = []
for ind in range(1, tempX.size):
    pair = [tempX[ind-1], tempX[ind]]
    pairs.append(pair)
#print(pairs)

# Значения вероятностей диапазона для таблицы
values = []
for ind in range(1, tempX.size):
    values.append(sum(tempP[:ind]))
#print(values)

df = pd.DataFrame(pairs, columns = ['x от', 'x до'])
df['F(x)'] = values
print('Таблица распределения:')
print(df, '\n') 

print('N значений случайной величины и их вероятности методом обратной функции:\n')

# Служебный массив вероятностей
probs = [round(i,1) for i in df['F(x)'].values.tolist()]
#print(probs)

# Служебный массив индексов
probsInd = np.random.randint(0, high=len(probs), size=N)
#print(probsInd)

# Служебная пара значения и вероятности
valProbList = []
for i in probsInd:
  tempList = []
  tempList.append(i)
  tempList.append(probs[i])
  valProbList.append(tempList)
#print(valProbList)

# Случайные значения по вероятности
randValues = []
for num in probsInd:
  pair = df.iloc[num,[0,1]].values.tolist()
  if (np.isneginf(pair[0])).any():
    pair[0]=-50
  if (np.isinf(pair[1])).any():
    pair[1]=50  
  randValues.append(np.random.randint(pair[0], pair[1]))
#print(randValues, '\n')

# Финальные значения и их вероятности
temp = [i for i in list(zip(*valProbList))[1]]
randValWithProbs = list(map(list, zip(randValues, temp)))
print(randValWithProbs,'\n')

print('2. Вывести q первых значений (q < N). \n')
print(randValues[:q],'\n')

print('3. Найти точные значения математического ожидания и дисперсии величины X. \n')
# Функция для высчитывания математического ожидания
def calc_Expectation(a, n):       
    # равная вероятность для каждого значения
    prb = 1 / n 
    # высчитывание математического ожидания 
    sum = 0
    for i in range(0, n): 
        sum += (a[i] * prb)  
    return np.round(float(sum), 3) 

# Параметры функции
n = len(randValues[:q]) 
a = randValues[:q] 
  
# Вызов функции  
expect = calc_Expectation(a, n) 
  
print( "Математическое ожидание X: ", expect) 

std = np.round(np.std(randValues[:q], axis=0), 3)
print( "Дисперсия X: ", std, '\n' ) 

print('4. Вычислить оценки математического ожидания и дисперсии случайной величины X, сравнить их с соответствующими точными значениями, сделать выводы.\n')
expectAssesment = np.round(np.mean(randValues[:q]), 3)
print( "Оценка математического ожидания X:", 
expectAssesment) 

expectStd = np.round(np.std(randValues[:q], axis=0, ddof=1), 3)
print( "Оценка дисперсии X: ", expectStd, "\n") 

print("Выводы:")
print("Если математическое ожидание оценки совпадает со значением оцениваемой величины, то такую оценку называют несмещенной.")
