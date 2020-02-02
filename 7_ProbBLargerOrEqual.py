"""
Теоремы сложения и умножения вероятностей
Задание 76 стр. 26

Доказать, что 
P A(B) >= 1 - P(not B)/P(A) 
Предполагается, что P(A)>0

@author: Ilia Gavrilov
"""
import numpy as np

# Вероятность события A
PA = np.round(np.random.uniform(0.1, 1), 1)

# Запуск цикла для генерирования вероятностей двух событий B и не B, где сумма B и не B равна 1
while True:
  PB = np.round(np.random.uniform(0, 1), 1)
  notPB = np.round((1 - PA), 1)
  if PB+notPB==1:
    break

print("Вероятности событий:\n", "A: ", PA)
print(" B: ", PB)
print(" not B: ", notPB, "\n")

print("Доказательство предположения:")
print("Условие PB >= 1 - notPB/PA является: ")
if PB >= 1 - notPB/PA:
  print(True)
  if PB > 1 - notPB/PA:
    print(PB, '> 1 - ', notPB, '/', PA)
  else:
    print(PB, '= 1 - ', notPB, '/', PA)
else:
  print(False)   
