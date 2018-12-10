import numpy as np
X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)
y = y/100

def sigmoid (x):#this function maps any value between 0 and 1
    return 1/(1 + np.exp(-x))

def derivatives_sigmoid(x):
    return x * (1 - x)

wh=np.random.uniform(size=(2,3))
bh=np.random.uniform(size=(1,3))
wout=np.random.uniform(size=(3,1))
bout=np.random.uniform(size=(1,1))


#draws a random range of numbers uniformly of dim x*y
for i in range(10000):
    #Forward Propogation
    inp1=np.dot(X,wh)
    inp=inp1 + bh
    hlayer = sigmoid(inp)

    out1=np.dot(hlayer,wout)
    out= out1+ bout
    output = sigmoid(out)

    #Backpropagation
    EO = y-output
    outgrad = derivatives_sigmoid(output)
    d_output = EO* outgrad

    EH = d_output.dot(wout.T)
    hiddengrad = derivatives_sigmoid(hlayer)#how much hidden layer wts contributed to error
    d_hiddenlayer = EH * hiddengrad


    wh += X.T.dot(d_hiddenlayer) *0.1
    bh += np.sum(d_hiddenlayer, axis=0,keepdims=True) *0.1

    wout += hlayer.T.dot(d_output) *0.1# dotproduct of nextlayererror and currentlayerop
    bout += np.sum(d_output, axis=0,keepdims=True) *0.1

print("Input: \n" + str(X))
print("Actual Output: \n" + str(y))
print("Predicted Output: \n" +str(output))
