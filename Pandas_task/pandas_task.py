import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

traveles_tab = pd.read_csv('travels.csv', delimiter = ';')
travel_agents_tab = pd.read_csv('travel_agents.csv', delimiter = ';')
sale_of_tour_packages_tab = pd.read_csv('sale_of_tour_packages.csv', delimiter = ';')

# Соеденим данные из 3 таблиц в одну:

tmp = pd.merge(sale_of_tour_packages_tab, travel_agents_tab)
allTab = pd.merge(tmp, traveles_tab)

# 1. Найти количество человек, совершивших путешествие в региональные центры.
# Таблицы региональных городов не предоставлено, поэтому определим их сами:

regionalCities = ['Москва', 'Вологда', 'Мурманск', 'Петрозаводск', 'Санкт-Петербург', 'Ярославль', 'Архангельск', 'Тверь',
'Сыктывкар', 'Иваново', 'Кострома', 'Псков']

# Отфильтруем таблицу таким образом, чтобы она включала данные региональных городов, затем посчитаем количество человек по проданным путевкам:

task1_filter = allTab['Город'].isin(regionalCities)
task1 = allTab[task1_filter]['Количество проданных путёвок'].sum()
print(task1)

# 2. Построить круговую диаграмму, отображающую общую стоимость путевок и стоимость путевок по каждому городу, 
# которые были проданы туроператором "Горизонт".

# Отберем строки, в которых речь идет о туроператоре "Горизонт"

task2_filter = allTab[allTab['Название'] == 'Горизонт']

# Сгруппируем эти строки по полю "Город" и найдем сумму по каждой группе

task2 = task2_filter.groupby('Город')['Стоимость, на 1 чел'].sum()

# Строим круговую диаграмму по этим данным
pie, ax1 = plt.subplots(figsize = [10, 6])
labels = task2.keys()
plt.pie(x = task2, autopct = "%.1f%%", labels = labels, pctdistance = 0.8)
plt.title("Туроператор Горизонт. Стоимость путевок", fontsize = 14)

# 3. Построить диаграмму, показывающую количество проданных путевок туроператором "Мечта" в каждый из дней.

# Отберем строки, в которых речь идет о туроператоре "Мечта"

task3_filter = allTab[allTab['Название'] == 'Мечта']
task3 = task2_filter.groupby('Дата')['Количество проданных путёвок'].sum()

# Видим, что количество дней примерно 90, строить по всем этим дням диаграмму - плохой вариант (получается каша)
# Предлагаю построить диаграмму не по каждому дню, а по каждому месяцу

# Создадим новый столбец, показывающий месяц:

def identifyMonth(month):
    if month[4] == '1':
        return 'Янаварь'
    if month[4] == '2':
        return 'Февраль'
    if month[4] == '3':
        return 'Март'

allTab['Месяц'] = allTab['Дата'].apply(identifyMonth)

# Сгурппируем данные по этому новому полю и в каждой группе подсчитаем количество элементов

task3 = allTab.groupby('Месяц')['Количество проданных путёвок'].count()

# Строим гистограмму по полученным данным

pie, ax2 = plt.subplots(figsize = [10, 6])
task3.plot.bar()
plt.title('Количество проданных путевок туроператором \"Мечта\" в каждый из месяцев', fontsize = 14)