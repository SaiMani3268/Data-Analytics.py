import numpy as np;

#printing arrays randomly with numpy

#print a range of numbers in a sequence
a1 = np.arange(0,100,20)
print(a1)

#printing 2d array with 1's
ones = np.ones((2,3,4))
print(ones)
print(ones.dtype)

#printing 2d array with 0's
zeros = np.zeros((2,3,4))
print(zeros)
print(zeros.dtype)

a2 = np.random.randint(0,10,size = (2,3,4))
print(a2)

a3 = np.random.random(size = (2,3,4))
print(a3)

#Pseudo random numbers
np.random.seed(seed = 20)
ps = np.random.randint(20,size = (3,3))
print(ps)
