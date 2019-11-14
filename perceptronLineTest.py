import numpy as np  
import matplotlib.pyplot as plt 
import pandas as pd

dataset=pd.read_csv('test.csv')

#function arriba 509x1,72y1  abajo 604x2,11y2
#
#    11-72
#m= -------
#    604-509
#m=-61/95
#
# y-72=(-61/95)(x-509)
#y=(-61/95)*x- (61/95)*509+72
# 
# Create plot
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

xline = np.linspace(450,620)
yline=(-61/95)*xline+ ((61/95)*509)+72

plt.plot(xline, yline, '-r', label='(-61/95)*xline+ ((61/95)*509)+72')

for index,row in dataset.iterrows():
    x, y,result = row['nota'],row['grado'],row['Resultado']
    color='red'
    if result==0:
        color='red'
    else:
        color='blue'
    ax.scatter(x, y, c=color)
    #ax.annotate("punto "+ str(x)+","+str(y),xy=(x,y))
plt.title('Matplot scatter plot')
plt.xlabel('x', color='#1C2833')
plt.ylabel('y', color='#1C2833')
plt.show()