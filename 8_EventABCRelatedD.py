"""
Теоремы сложения и умножения вероятностей
Задание 77 стр. 26

Наступление события ABC необходимо влечет наступление события D. Доказать, что
P(A) + P(B) + P(C) - P(D) <= 2 

@author: Ilia Gavrilov
"""
import numpy as np

# Генерирование вероятностей событий
while True:
    a = np.round(np.random.uniform(0, 1), 1)
    b = np.round((1 - a), 1)
    c = np.round(np.random.uniform(0, max(a,b)), 1)
    d = np.round((1- (b+c)), 1)
    if b+c+d == 1 and all(i > 0 for i in [b,c,d]):
        PA = b
        PB = c
        PC = d
        break

PD = np.round(np.random.uniform(0, 1), 1)

print("Вероятности событий:") 
print('A: ', PA)
print('B: ', PB)
print('C: ', PC)
print('D: ', PD, "\n")

print("Наступление события ABC необходимо влечет наступление события D, следовательно:") 
print("Условие P(D) >= P(ABC)")
if PD >= round(PA*PB*PC, 2) - round(PA*PB*PC, 2) % 0.1:
  print(True)
  if PD > round(PA*PB*PC, 2) - round(PA*PB*PC, 2) % 0.1:
    print(PD, " > ",  PA, " * ", PB, " * ", PC, '\n')
  else:
    print(PD, " = ",  PA, " * ", PB, " * ", PC, '\n')
else:
  print(False, '\n')   

print("Доказательство предположения:")
print("Условие P(A) + P(B) + P(C) - P(D) <= 2 является:")
if PA + PB + PC - PD <= 2:
  print(True)
  if PA + PB + PC - PD < 2:
    print(PA, " + ", PB, " + ", PC, " - ", PD, " < 2")
  else:
    print(PA, " + ", PB, " + ", PC, " - ", PD, " = 2")
else:
  print(False, '\n')
