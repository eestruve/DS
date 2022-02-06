import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
from numpy import median

df = pd.read_csv('test_cluster.csv', encoding='cp1251', sep=';')

sns.set(style='darkgrid')

# sns.relplot(
#     x='age',
#     y='full_mob',
#     data=df.query("index<300"),
#     kind='line'
#  )
# plt.title('Линейная диаграмма', size=20, color='g');
# plt.show()

# gender_order = ['<100', 'Mega', '100-500', '1M+', '500-1000' ]
# sns.relplot(
#     x='age',
#     y='full_mob',
#     hue ='city_type',
#     hue_order = gender_order,
#     data=df.query("index < 300"), kind='line')
# plt.title('Линейная диаграмма с параметром hue=daywk', size=20, color='g');
# plt.show()

# sns.relplot(
#     x='age',
#     y='full_mob',
#     hue='city_type',
#     data = df,
#     kind='line',
#     err_style="bars",
#     ci=99)   # Standard Errors
# plt.title('Линейная диаграмма со стандартной ошибкой bar and hue', size=20, color='g');
# plt.show()

# sns.relplot(
#     x='age',
#     y='full_mob',
#     hue='gender',
#     style='city_type',
#     kind='line',
#     ci='sd',
#     data= df)
# plt.title('Линейная диаграмма с параметрами hue и style', size=20, color='g');
# plt.legend();
# plt.show()

# sns.relplot(
#     x='age',
#     y='full_mob',
#     data= df,
# #     kind='scatter'
# #     kind='line' loan_balance_0m
# )
# plt.title('Диаграмма рассеяния', size=20, color='g');
# plt.show()

# sns.relplot(
#     x='age',
#     y='full_mob',
#     hue='gender',
#     data= df)
# plt.title('Диаграмма рассеяния с параметром hue', size=20, color='g');
# plt.show()

# sns.relplot(
#     x='age',
#     y='full_mob',
#     hue='city_type',
#     style='gender',
#     markers=['^', 'D', 'o'],
#     data= df)
# plt.title('Диаграмма рассеяния с параметрами hue и style', size=20, color='g');
# plt.show()


# day_order = ['F', 'M', 'X']
# sns.relplot(
#     x='full_mob',
#     y='age',
#     hue='city_type',
#     col='gender',
#     col_wrap=3,
#     col_order=day_order,
#     data= df,
#     height=5
#    );
# plt.show()

# day_order = ['<100', 'Mega', '100-500', '1M+', '500-1000']
# sns.relplot(
#     x='age',
#     y='full_mob',
#     col='city_type',
#     col_order=day_order,
#     row='gender',
#     row_order=['X', 'M', 'F'],
#     data=df,
#     height=3);
# plt.show()
#
# sns.set(style="ticks", color_codes=True)
#
# day_order = ['<100', 'Mega', '100-500', '1M+', '500-1000']
# sns.catplot(
#     x='city_type',
#     y='full_mob',
#     data=df,
#     hue='gender',    # оба на одном графике разными цветами
#     order=day_order,
#     jitter=0.01,
#     height=4,
#     aspect=2,
#     kind='strip',
#     dodge=True)
# # Можно использовать dodge=True чтобы не накладывать показатели друг на друга, а выстроить рядом друг с другом
# plt.title('stripplot jitter=0.05', size=20, color='g');
# plt.show()

# sns.catplot(
#     x='city_type',
#     y='full_mob',
#     data=df.query("city_type != '100-500'"),
#     order=['<100', 'Mega', '1M+', '500-1000'],
#     palette='Set1',
# #     jitter=False, выстраивает все точки в линию
#     height=4,
#     aspect=2);
#
# plt.title('stripplot с параметром jitter, заданным по умолчанию', size=20, color='g');
# plt.show()
#
# day_order = ['<100', 'Mega', '100-500', '1M+', '500-1000']
# sns.catplot(
#     x='city_type',
#     y='full_mob',
#     data=df.query("index < 300"),
#     order=day_order,
#     hue='gender',
#     kind='swarm',
#     height=4,
#     aspect=2)
# plt.title('swarmplot', size=20, color='g');
# plt.show()

# sns.set(style='darkgrid')
# day_order = ['<100', 'Mega', '100-500', '1M+', '500-1000']
# sns.catplot(
#     x='city_type',
#     y='full_mob',
#     data=df,
#     kind='box',
#     height=4,
#     aspect=2
# );
# plt.show()

# sns.catplot(
#     x='city_type',
#     y='full_mob',
#     data=df,
#     kind='box',
#     hue='gender',
#     height=4,
#     aspect=2);
# plt.show()

# day_order = ['<100', 'Mega', '100-500', '1M+', '500-1000']
# sns.catplot(
#     x='city_type',
#     y='full_mob',
#     data=df,
#     kind='box',
#     hue='gender',
#     order=day_order,
#     height=4,
#     aspect=2);
# plt.show()

# sns.catplot(
#     x='city_type',
#     y='full_mob',
#     data=df,
#     kind='boxen',
#     height=4,
#     aspect=2);
# plt.show()

# sns.catplot(
#     x='city_type',
#     y='full_mob',
#     data=df,
#     kind='boxen',
#     hue='gender',
#     height=4,
#     aspect=2);
# plt.show()
#
# sns.catplot(
#     x='full_mob',
#     y='city_type',
#     data=df,
#     kind='boxen',
#     hue='gender',
#     height=4,
#     aspect=2);
# plt.show()




# plt.figure(figsize=(9,4))
# b = sns.barplot(
#     x='city_type',
#     y='full_mob',
#     data=df,
#     estimator=sum,
#     palette='husl')
#
# b.set(yscale='log', ylim=[50000, 1000000])
# sns.despine()
#
# for bar in b.patches:
#     b.annotate(
#         "{:,}".format(bar.get_height()),
#         (bar.get_x()+bar.get_width()/2.,
#         bar.get_height()),
#         ha='center',
#         va='center',
#         xytext=(0,10),
#         textcoords='offset points',
#         color='b',
#         weight='bold'
#     )
#
# plt.title('1. Столбиковая диаграмма: длинный формат с аннотациями(estimator=sum)', size=15, color='g',
#           weight='bold');
# plt.show()

# sns.catplot(
#     data=df,
#     kind='bar',
#     height=4,
#     aspect=2,
#     order=['td_balance_0m', 'ml_balance'],
#     palette="Set1"
# );
# plt.title('2. Столбиковая диаграмма: Широкий формат таблицы с предопределенной палитрой цветов', size=15, color='g',
#           weight='bold');
# plt.show()

# sns.catplot(
#     x='city_type',
#     y='age',
#     data=df,
#     kind='bar',
#     hue='gender',
#     hue_order=['X','F', 'M'],
#     palette={"X": "r", "F": "indigo", 'M': 'grey' },
#     estimator=median,
#     capsize=0.2,
#     height=4,
#     aspect=2);
#
# plt.title('3. Столбиковая диаграмма: длинный формат данных, (estimator=median) и  кастомная палитра',
#           size=15,
#           color='g',
#           weight='bold');
# plt.show()

# day_order = ['<100', 'Mega', '100-500', '1M+', '500-1000']
# sns.catplot(
#     x='city_type',
#     y='age',
#     data=df,
#     kind='bar',
#     hue='gender',
#     ci='sd',
#     estimator=len,
#     capsize=0.25,
#     errcolor='m',
#     errwidth=1,
#     hue_order=['X','M', 'F'],
#     palette="muted",
#     order=day_order,
#     height=4,
#     aspect=2);
# plt.title('4. Столбиковая диаграмма, (estimator=len(count), errwidth=5, errcolor=m)',
#           size=15,
#           color='g',
#           weight='bold'
#          );
# plt.show()

# sns.catplot(x='city_type',
#             data=df,
#             kind='count',
#             height=4,
#             aspect=2
#            );  # long form data frame
# plt.title('5. Count Plot - Продажи по продуктам', size=15, color='g', weight='bold');
# plt.show()

# sns.catplot(
#     x='city_type',
#     data=df,
#     kind='count',
#     hue='gender',
#     hue_order=['X','F', 'M'],
#     palette={"X": "r", "F": "indigo", 'M': 'grey'},
#     height=4,
#     aspect=2);
# plt.title('6. Count Plot, hue=Promotion, custom palette', size=15, color='g', weight='bold');
# plt.show()

# day_order = ['<100', 'Mega', '100-500', '1M+', '500-1000']
# sns.catplot(
#     x='city_type',
#     data=df,
#     kind='count',
#     hue='gender',
#     hue_order=['X','F', 'M'],
#     palette="Set2",
#     order=day_order,
#     height=4,
#     aspect=2);
# plt.title('7. Count Plot: Продажи по дням недели', size=15, color='g', weight='bold');
# plt.show()

# sns.catplot(
#     x='gender',
#     y='age',
#     data=df,
#     kind='violin',
#     height=6,
#     aspect=2)
# plt.title('1. Горизонтальная диаграмма - виолончели', size=15, color='g', weight='bold');
# plt.show()

# sns.catplot(
#     x='city_type',
#     y='age',
#     data=df,
#     kind='violin',
#     hue='gender',
#     hue_order=['X','F'],
#     split=True,
#     height=4,
#     aspect=2)
#
# plt.title('2. Вертикальные виолончели с параметрами hue=Promotion, split=True', size=15, color='g', weight='bold');
# plt.show()


# day_order = ['<100', 'Mega', '100-500', '1M+', '500-1000']
# sns.catplot(
#     x='city_type',
#     y='age',
#     data=df,
#     kind='violin',
#     order=day_order,
#     hue='gender',
#     hue_order=["X", "F"],
#     split=True,
#     inner="stick",
#     palette="pastel",
#     height=4,
#     aspect=2)
# plt.title('3. Виолончели с параметрами hue=Promotion, split=True, inner=stick', size=15, color='g', weight='bold');
# plt.show()

#
# sns.catplot(
#     x='gender',
#     y='age',
#     data=df, # long form data frame
#     kind='point',
#     markers='D',
#     ci='sd',
#     height=4,
#     aspect=2)
# plt.title('2.  Точечная диаграмма с алмазным маркером и SD в доверительном интервале', size=15, color='g', weight='bold');
# plt.show()

# sns.catplot(
#     x='full_mob',
#     y='age',
#     data=df,
#     kind='point',
#     hue='gender',
#     hue_order=['F','M', 'X'],
#     palette={"F": "r", "M": "indigo", 'X': 'gray'},
#     markers=["^", "o", '+'],
#     linestyles=["-", "--", ':'],
#     ci=None,
#     col='city_type',
#     col_wrap=3,
#     height=4,
#     aspect=2,
#     scale=1.5)
# plt.suptitle("3. Точечная диаграмма с параметрами hue=Promotion, col='daywk'", size=15, color='g', weight='bold')
# plt.tight_layout(pad=5,w_pad=0.25, h_pad=0.25);
# plt.show()

# sns.set(style='whitegrid', color_codes=True)
#
# sns.distplot(
#     df.age,
#     color='g',
#     rug=True,
#     rug_kws={"color": 'm', "height": 0.1}
# )
# plt.title('1.Диаграмма распределения продаж кофе с параметром rug=True', size=15, color='g', weight='bold')
# plt.show();


# sns.distplot(
#     df.age,
#     vertical=True,                #hist=False
#     hist_kws={"histtype": "step", "linewidth": 3, "alpha": 0.7, "color": "indigo", "label": "Histogram"},
#     kde_kws={"shade": True, "color": "orange", "lw": 3, "label": "KDE"})
# plt.title('2. Горизонтальная диаграмма распределения продаж печенек', size=15, color='g', weight='bold')
# plt.show();

#
# df_items = df.loc[:,['age', 'city_type', 'gender']]
# sns.pairplot(
#     df_items,
#     hue='gender',
#     kind='reg'
# )
# plt.show();

