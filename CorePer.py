import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.figure(figsize=(10,6))

np.random.seed(42)

df = pd.read_csv("data.csv",sep=",",names=["p","q","y"])
df_p_true = df[df['y']==1]['p']
df_q_true = df[df['y']==1]['q']
df_p_false = df[df['y']==0]['p']
df_q_false = df[df['y']==0]['q']

def stepFunction(t):    
    return 1 if t >= 0 else 0
def prediction(X,W,b):
    return stepFunction((np.matmul(X,W)+b)[0])

def plot_points(X, y):
    admitted = X[np.argwhere(y==1)]
    rejected = X[np.argwhere(y==0)]
    plt.scatter([s[0][0] for s in rejected], [s[0][1] for s in rejected], s = 25, color = 'green', edgecolor = 'k')
    plt.scatter([s[0][0] for s in admitted], [s[0][1] for s in admitted], s = 25, color = 'orange', edgecolor = 'k')

def display(m, b, color='y--'):
    plt.xlim(-0.05,1.05)
    plt.ylim(-0.05,1.05)
    x = np.arange(-10, 10, 0.1)
    plt.plot(x, m*x+b, color)

def perceptronStep(X, y, W, b, learn_rate = 0.01):
    for i in range(len(X)):
        y_hat = prediction(X[i],W,b)
        if y[i]-y_hat == 1:
            W[0] += X[i][0]*learn_rate
            W[1] += X[i][1]*learn_rate
            b += learn_rate
        elif y[i]-y_hat == -1:
            W[0] -= X[i][0]*learn_rate
            W[1] -= X[i][1]*learn_rate
            b -= learn_rate
    return W, b
def trainPerceptronAlgorithm(X, y, learn_rate = 0.01, num_epochs = 25):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2,1))
    b = np.random.rand(1)[0] + x_max    
    boundary_lines = []
    for i in range(num_epochs):                
        weights, bias = perceptronStep(X, y, W, b, learn_rate)        
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
        display(-weights[0]/weights[1], -bias/weights[1])
        
    display(-weights[0]/weights[1], -bias/weights[1], 'black')    
    plot_points(X, y)    
    return boundary_lines

plt.scatter(df_p_true,df_q_true,c='green',label="True")
plt.scatter(df_p_false,df_q_false,c='orange',label="False")
plt.title("Scatter plot for the data.")
plt.ylim(-0.20,1.20)
plt.legend()

X= df[['p','q']].values
y = df['y'].values
boundryLines = trainPerceptronAlgorithm(X,y)
plt.show()