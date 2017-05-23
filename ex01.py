import numpy as np
x = np.array([1,5,2])
y = np.array([7,4,1])
z = x + y
print("Simple Array Addition --> ", z)
print("Simple Array Multiplication --> ", x*y)

p = np.matrix( ((2,3), (3, 5)) )
q = np.matrix( ((1,2), (5, -1)) )

print("Matrix Multiplication --> ", p*q)

x = 43
x = x + 1
print (x)

