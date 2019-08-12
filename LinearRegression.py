import pandas as pd
import matplotlib

matplotlib.use('WebAgg')
import matplotlib.pyplot as plt


def step_gradient(x, y, m, b):
    alpha =0.0001

    mGrad = 0
    bGrad = 0
    for i in range(x.shape[0]):
        xp = x[i]
        yp = y[i]
        bGrad += (yp - (m*xp + b))
        mGrad += (xp*(yp-(m*xp+b)))

        print(mGrad, bGrad)
    #print(mGrad, bGrad)
    mGrad *=-2/x.shape[0]
    bGrad *= -2/x.shape[0]

    newm = m-(alpha*mGrad)
    newb = b-(alpha*bGrad)

    return [newm,newb]

def gradient_descent(x, y, iterations):
    m = 0
    b = 0

    for i in range(iterations):
        yr = m*x + b
        plt.plot(x, yr)
        plt.scatter(x, y, edgecolors='red')
        plt.show()
        m, b = step_gradient(x, y, m, b)
    return [m, b]


data = pd.read_csv('train.csv')
testData = pd.read_csv('test.csv')
x = data['x'].head(200)
y = data['y'].head(200)
xt = testData['x']
yt = testData['y']


mans,bans = gradient_descent(x,y,30)
yr = mans*x + bans
print("ans: m : ",mans,"b : ",bans)




