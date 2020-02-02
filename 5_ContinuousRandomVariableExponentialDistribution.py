print("""
В.Е. Гмурман Руководство к решению задач по теории вероятностей к математической статистике

Создать программу, которая которая моделирует случайную величину, распределенную по показательному закону

Задание 691 стр. 299 

@author: Ilia Gavrilov
""")

from scipy.stats import expon
import matplotlib.pyplot as plt
import numpy as np 

fig, ax = plt.subplots(1, 1)

# 1. Высчитываем первые несколько моментов
mean, var, skew, kurt = expon.stats(moments='mvsk')

# 2. Функция плотности вероятности (pdf)
x = np.linspace(expon.ppf(0.01), expon.ppf(0.99), 100)
ax.plot(x, expon.pdf(x), 'r-', lw=5, alpha=0.6, label='expon pdf')

# 3. Фиксируем распределение
rv = expon()
ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

# 4. Проверка точности
vals = expon.ppf([0.001, 0.5, 0.999])
np.allclose([0.001, 0.5, 0.999], expon.cdf(vals))

# 5. Генерирование случайных величин
r = expon.rvs(size=1000)
print('Массив случайных величин по показательному закону: \n', r[:15])
print('Результаты рассчета представлены на графике ExponentialDistribPlotV2.png')
# 6. Показываем и сравниваем графики
ax.hist(r, density=True, histtype='stepfilled', alpha=0.2)
ax.legend(loc='best', frameon=False)
label = 'Распределение случайных величин по показательному закону'
plt.title(label, fontdict=None, loc='center', pad=None)
plt.show()

plt.savefig('ExponentialDistribPlotV2.png')
