print("""
А.В. Иванов, А.П. Иванова Моделирование случайных величин, систем массового обслуживания и случайных процессов

Создать программу, которая выводит выборку дискретных случайных величин стр. 6 - 9

@author: Ilia Gavrilov
""")

import numpy as np

# Моделирование дискретной случайной величины с помощью
# функции распределения случайной величины
X  = np.sort(np.random.randint(10, size=100))
print("Отсортированный массив дискретных величин: \n", X)

# Реализация метода моделирования дискретной случайной
# величины, заданной своим законом распределения

# Функция подсчета частоты каждого значения
def frequencies(values):
    frequencies = {}
    for v in values:
        if v in frequencies:
            frequencies[v] += 1
        else:
            frequencies[v] = 1
    return frequencies

# Функция преобразования частоты в вероятности
def probabilities(sample, freqs):
    probs = {}
    for k,v in freqs.items():
        probs[k] = round(v/len(sample),2)
    return probs


# Получение вероятностей
probs = probabilities(X, frequencies(X))
print("Словарь дискретных величин и их вероятностей: \n", probs )


# Получение выборок дискретных случайных величин 
sample = np.random.choice(list(set(X)), 5, p=list(probs.values()))
print("Выборка случайных величин: \n", sample )
