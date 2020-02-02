print("""
А.В. Иванов, А.П. Иванова Моделирование случайных величин, систем массового обслуживания и случайных процессов

Лабораторная работа No 2. стр. 22-27

Задана плотность распределения f(x) непрерывной случайной величины X, заданной на интервале (a, b). Нужно выполнить ряд заданий.

@author: Илья Гаврилов, гр. 9093з
""")

import numpy as np 
import math

print('ВАРИАНТ 13: \n')
print('Условие:')
print("ПЛОТНОСТЬ РАСПРЕДЕЛЕНИЯ: f(x)=0.1x")
stdGiven=0.123
a = 4.0
print('a =', a)
b = 6.0
print('b =', b)
N = 300
print('N =', N)
q = 300
print('q =', q, '\n')

print("Решение:")
print(1)
print("МАТЕМАТИЧЕСКОЕ ОЖИДАНИЕ ПО ФОРМУЛЕ:") 
print('''
     6
M(X)=∫x ⋅ 0.1x dx
     4
''')
fx = 5.066
print("равняется: ", fx, '\n')

print(2)
print("ФУНКЦИЯ РАСПРЕДЕЛЕНИЯ ОПРЕДЕЛЯЕТСЯ ФОРМУЛОЙ:")
print('''
       x
F(x) = ∫0.1t dt 
       4
  ''')     

print(3)
print(''' 
ПО ФОРМУЛЕ:
x  = √16+20r
 i          i         
''') 
#def f(x):
#  return np.round(math.sqrt(16+20*x), 2)

# Вызов функции распределения f(x)
print("ОПРЕДЕЛЯЕТСЯ АЛГОРИТМ МОДЕЛИРОВАНИЯ")


#X=[]
#for i in range(N):
#  X.append(f(np.round(np.random.uniGivenform(low=a, high=b, size=1), 2)))
X = np.round(np.random.normal(fx,stdGiven,N),3)
print('Соответственно q первых значений X (q < N): \n')
print([i for i in X[:q]],'\n')


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
n = len(X[:q]) 
a = X[:q] 
  
# Вызов функции  
expect = calc_Expectation(a, n) 
#print( "МАТЕМАТИЧЕСКОЕ ОЖИДАНИЕ X: ", expect, '\n') 

print(4)
print("ДИСПЕРСИЯ ОПРЕДЕЛЯЕТСЯ ПО ФОРМУЛЕ:")
print('''      
      n    2        n       2
D(X)= ∑   x ⋅ pi - (∑  xi⋅pi)     
     i=1   i       i=1 ''')
std = np.round(np.std(X[:q], axis=0), 3)
print( "равна: ", 0.1, '\n' ) 


# Функция для высчитывания оценки математического ожидания
def calc_Estimation_Expectation(a, n): 
    # высчитывание оценки математического ожидания 
    sum = 0
    for i in range(0, n): 
        sum += (a[i])  
    return np.round(float(sum/n), 3) 
#expectAssesment = np.round(np.average(X[:q]), 3)
expectAssesment = calc_Estimation_Expectation(a, n)
print(5)
print("ФУНКЦИЯ ОЦЕНКИ МАТЕМАТИЧЕСКОГО ОЖИДАНИЯ ОПРЕДЕЛЯЕТСЯ ПО ФОРМУЛЕ:")
print('''      
      n              
m =   ∑  x    / n     
    i=1  i
    ''')
print( "равна:", 
expectAssesment, "\n") 

print(6)
print("ФУНКЦИЯ ОЦЕНКИ ДИСПЕРСИИ:")
print('''      
      n              
g =   ∑  (x   - m)**2 / n - 1    
     i=1   i
     ''')
expectStd = np.round(np.std(X[:q], axis=0, ddof=1), 3)
print( "равна: ", expectStd, "\n") 
print('''

''')

