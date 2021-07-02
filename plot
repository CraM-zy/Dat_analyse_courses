import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt

student_perfomance = pd.read_csv('/Users/cram/Downloads/StudentsPerformance.csv')
student_perfomance = student_perfomance.rename(columns=lambda x: x.replace(' ', '_'))
student_perfomance.math_score.hist()

student_perfomance.plot.scatter(x='math_score', y='reading_score')

ax = sns.lmplot(x='math_score', y='reading_score', hue='gender', data=student_perfomance, fit_reg=False)
ax.set_xlabels('Math')
ax.set_ylabels('Read')
#######################################################################################################

df = pd.read_csv("dataset_209770_6-3.txt", sep=" ")
graf = sns.lmplot(x='x', y='y', data = df)
#######################################################################################################

matr = pd.read_csv('/Users/cram/Downloads/genome_matrix.csv', index_col=0 )
g = sns.heatmap(data=matr, cmap="viridis" )
g.xaxis.set_ticks_position('top')
g.xaxis.set_tick_params(rotation=90)
#######################################################################################################

flowers = pd.read_csv('/Users/cram/Downloads/iris.csv')
sns.distplot(flowers['petal width'], color = "blue")
sns.distplot(flowers['petal length'], color ="green")
sns.distplot(flowers['sepal width'], color = "yellow")
sns.distplot(flowers['sepal length'], color = "orange")

flowers2 = flowers.rename(columns=lambda x: x.replace(' ', '_'))
pl=sns.pairplot(flowers2)
