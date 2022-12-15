import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# Графики встраиваются в документ, а не отображаются в отдельном окне

x = np.linspace(0.0, 2 * np.pi, 100) #последовательность от нуля до 2х пи засунутая в 100 значений
y1 = np.cos(x)
y2 = np.sin(x)

fig = plt.figure()  # Создаем холст рисунка
plt.plot(x, y1, '+', c='red')  # Строим график cos
plt.plot(x, y2, c='blue')  # Строим график sin


plt.grid(True)  # Построение сетки на графике

plt.show()  # Отображение рисунка
