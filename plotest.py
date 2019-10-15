import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None
df_can = pd.read_csv('Libro1.csv',index_col='Alumno')
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, facecolor="1.0")
df_can.loc[df_can['Resultado']==1,'color']='blue' 
df_can.loc[df_can['Resultado']==0,'color']='red'
for data in df_can:
    x, y,color = df_can['Nota'],df_can['Grado'],df_can['color']
    ax.scatter(x, y,  alpha=0.8,edgecolors='none', s=30,c=color)
plt.title('Matplot scatter plot')
plt.show()