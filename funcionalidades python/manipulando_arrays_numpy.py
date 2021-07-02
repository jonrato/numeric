#manipulando arrays numpy
print("manipulando arrays numpy")

import numpy as np
a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])
suma = a + b # Soma
difference = a - b # Subtração
product = a * b # Multiplicação
quotient = a / b # Divisão
print('Sum = \n', + suma)
print('\n')
print('Difference = \n', + difference)
print('\n')
print('Product = \n', + product)
print('\n')
print('Quotient = \n', + quotient)
#matrix product
print("matrix product")
matrix_product = a.dot(b) 
print('Matrix Product = \n', + matrix_product)