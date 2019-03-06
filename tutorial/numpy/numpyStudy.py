# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt

# a = np.array([[1.0, 2.0], [3.0, 4.0]])
# b = np.array([[5.0, 6.0], [7.0, 8.0]])
# sum = a + b
# difference = a - b
# product = a * b
# quotient = a / b
# print("Sum = \n", sum)
# print ("Difference = \n", difference)
# print("Product = \n", product)
# print("Quotient = \n", quotient)
#
# a = np.arange(25)
# a = a.reshape((5, 5))
# b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
#               4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
#               56, 3, 56, 44, 78])
# b = b.reshape((5,5))
a = np.arange(0, 100, 10)
mask=a >= 50
print(mask)
print(a[mask])