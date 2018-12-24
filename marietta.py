import numpy as np
from scipy.misc import derivative
from matplotlib import pylab as plt


def f(x):
    return (x + 5)**2

xn = 0
yn = f(xn)

x = np.linspace(-15, 15, 100)
y = [f(xn) for xn in x]

xt = int(input('Введите значение Х в интервале от -15 до 15: '))
cr = derivative(f, xt)

if cr > 0:
    text = 'В данной точке функция возрастает и производная в точке равна: ', cr
elif cr < 0:
    text = 'В данной точке функция убывает и производная в точке равна: ', cr
else:
    text = 'В данной точке мы находимся в локальном минимуме и производная в точке равна: 0'

fig, ax = plt.subplots(figsize = (8, 5))
ax.scatter(xt, f(xt), color = 'red')
ax.plot(x, y)
ax.set_title(text)
plt.show()