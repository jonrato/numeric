###### EP1 ######

#Nome: Andressa Bueno Gonçalves
#NºUSP:11374769
#Turma: 6
###########################3
#Nome: Ana Alice Clímaco Barbosa
#NºUSP: 11302348
#Turma: 7

import numpy as np
import time
import math

ak = 2
bk = -1
e = 10**-6
uk = 0
n = np.array([4,8,16,32])
print(n)
pi = math.pi
seno = math.sin
coseno = math.cos




def lambda_j():
	 
	i = 0 #contador dos elementos de n
	j = 1 # j
	
	u1 = j*pi/n[1]+1
	u2 = n[i]*j*pi/n[i]+1
	
	while(i<= 3): #laço que faz a contagem dos elementos da posição 0 a 3
		for i in range(n[i]): #laço de repetição que faz a varredura de cada valor de n na matriz
								#pelo índice. Ex:n[0],n[1],n[2],n[3]
			
			lamb_j = 2*(1 - coseno(u1)) #var lambdaJ
			print("lambda jota")
			print(lamb_j)
			
		for j in n:
			vj = seno(u2) #autovalores correspondentes
			print("vj")
			print(vj)
			
			vj = seno(u2) #autovalores correspondentes
			print("vj")
			print(vj)
			
		i=i+1
		j = j+1
		print(lamb_j)
		print(vj)

	return lamb_j, vj

print(lambda_j())

def I():
	identity(3, dtype=float)
	array([[ 1.,  0.,  0.],
	       [ 0.,  1.,  0.],
	       [ 0.,  0.,  1.]])
	return identity

def questaoA(lamb_j,vj):
	k = 0
	Q = np.array([coseno(pi)])
	i_n = 0
	i_mm = 0
	A = (lamb_j*vj)
	R = Q*Q*A
	

	A = (R**(k))*(Q**(k)) +uk*I()
	print(A**(k+1))
	return print(A**(k+1))

print(questaoA)

def X():
	X0 = np.array([-2,-3,-1,-3,-1]) #teste1
	X1 = np.array([1,10,-4,3,-2]) #teste2
	X2 = 0 #teste3
	return X0,X1,X2
def questaoB(X):

	id = 0
	x = Simbol('x')
	
	for id in range(X0[id]):
		dX = X[id].diff(x)
		dXdX = dX.diff(x)
		res = dXdX + A*X()
		return print(res)

		id = id+1
		print(X[id])

	id = 0
	for id in range(X1[id]):


def questaoC(lamb_j,vj,Ident):
	print("Questao C")


print("EP1")
question = input(print("Escolha uma Questao:a para A; b para B; c para C"))

if question == 'a':

	print("questao A")
	def lambda_j():
	 
		i = 0 #contador dos elementos de n
		j = 1 # j
		
		u1 = j*pi/n[1]+1
		u2 = n[i]*j*pi/n[i]+1
	
		while(i< 3):
			for i in range(n[i]):
				
				lamb_j = 2*(1 - coseno(u1)) #var lambdaJ
				print("lambda jota")
				print(lamb_j)
				
			for j in n:
				
				vj = seno(u2) #autovalores correspondentes
				print("vj")
				print(vj)
				
			i=i+1
			j = j+1
			print(lamb_j)
			print(vj)

		return lamb_j, vj
	print(questaoA)

	def I(Ident):
		Ident = ([2,0],[0,2])
		return Ident

	def questaoA(lamb_j,vj,Ident):
		k = 0
		Q = np.array([coseno(pi)])
		i_n = 0
		i_mm = 0
		A = (lamb_j*vj)
		R = Q*Q*A
		

		A = (R**(k))*(Q**(k)) +uk*I(Ident)
		print(A**(k+1))
		return print(A**(k+1))



	
elif question == 'b':
	print("questao B")
	print(questaoB)
elif question == 'c':
	print("questao C")
	print(questaoB)
else:
	print("opcao invalida")