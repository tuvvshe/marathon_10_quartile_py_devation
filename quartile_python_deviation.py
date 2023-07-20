import numpy as np
data = list(range(50, 200, 3))
print(data)

Q1=np.quantile(data, 0.33)
Q2=np.quantile(data, 0.50)
Q3=np.quantile(data, 0.75)

print("QUARTILE 1 : ", Q1)
print("QUARTILE 2 : ", Q2)
print("QUARTILE 3 : ", Q3)

def QuatileDeviation(a, b):
    return(a - b)/2
print(QuatileDeviation(Q3, Q1))