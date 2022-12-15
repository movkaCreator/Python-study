import numpy as np
from numpy import linalg as la

array = np.random.randint(0, 100, (4, 9))
print(array)  # 1 Сгенерировать матрицу размером 4 × 9, заполненную целыми числами (от 0 до 100 это я сам уже) .
print()

print(array[1][5])  # Вывести на экран элемент с индексами [2, 6].
print()

print(array[2][1::2])  # Вывести на экран каждый второй элемент третьей строки матрицы.
print()

print(array[3][::-1])  # Вывести на экран элементы последнего столбца в обратном порядке.
# или так   print(array[len(array) - 1][::-1])
print()

array.shape = (6, 6)
print(array)  # Изменить форму матрицы с 4 × 9 на 6 × 6.
print()

print(array**2) # Возвести каждый элемент матрицы в заданную степень.
print()

glDiag = np.diag(array)
print(glDiag)
print(glDiag.min(0))  # Найти минимум на главной диагонали.
print()

print(array[4].max(0)) # Найти максимальный элемент в предпоследнем столбце.
# или так print(array[len(array) - 2].max(0))
print()

array1D = array.reshape(-1, )
# array1D = array.reshape(36,) тут просто сами посчитали кол-во элементов, а выше автоматически
print(array1D)
res = True
for i in range(0, len(array) - 1):
    if array1D[i] < array1D[i + 1]:
        res = False
print(res)  # Определить, образуют ли элементы сжатого до одной оси массива невозрастающую последовательность.
print()

pobDiad = np.diagonal(np.flip(array, axis=1))
prod = 1
for x in pobDiad:
    if x != 0:
        prod *= x
print(pobDiad)
print(prod)  # Подсчитать произведение ненулевых элементов на побочной диагонали.