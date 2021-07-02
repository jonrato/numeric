import numpy as np

#Shape
my_array = np.array([[1,2,3,4,6],[1,2,3,4,5]]) #2linhas, 5 colunas
print("array shape: 2 linhas, 5 colunas")
print(my_array.shape)
#Range-Reshape
print("range reshape: 3 linhas, 2 colunas")
a = np.arange(6).reshape((3,2))
print(a)
#atrbuir outro valor a um elemento de um array
my_array[0] = -1 
print("atrbuir outro valor a um elemento de um array")
print(my_array)
#Array numpy vazia
print("Array numpy vazia")
x = np.empty([3,2], dtype = int) 
print(x)
#array numpy de zeros
print("Array numpy de zeros")
my_new_array = np.zeros((3,5)) 
print(my_new_array)
#array de valores aleatorios
print("array de valores aleatorios")
my_random_array = np.random.random((3,5))
print(my_random_array)
#valores aleatorios entre 1 e 10
print("valores aleatorios entre 1 e 10")
v = np.floor(10*np.random.random((3,4)))
print(v)
#fatiamento de elementos
print("fatiamento de elementos")
my_array2 = np.array([3, 2, 8, 22, 127]) 
print(my_array2[2:4])
#array numpy bidimensional
print("array numpy bidimensional")
my_array3 = np.zeros((2,3))
print(my_array3)
#array numpy bidimensional ones
print("array numpy bidimensional ones")
my_array4 = np.ones((2,4))
print(my_array4)
#coluna 0 do índice e na coluna do índice 1
print("coluna 0 do índice e na coluna do índice 1")
my_array = np.array([[4, 5], [6, 1]])
print(my_array[0][1])
#Aqui, como pode ser visto, a segunda coluna é composta de dois elementos: 5 e 1
print("Aqui, como pode ser visto, a segunda coluna é composta de dois elementos: 5 e 1")
my_array_column_2 = my_array[:, 1]
print(my_array_column_2)
