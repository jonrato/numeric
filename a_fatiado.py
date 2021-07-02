import numpy as np
import time
import math
import ast

ak = 2
bk = -1
e = 10**-6
uk = 0


pi = math.pi
seno = math.sin
coseno = math.cos


def lambda_j():
	ak = 2
	bk = -1
	e = 10**(-6)
	uk = 0


	pi = math.pi
	seno = math.sin
	coseno = math.cos


	m = input("Digite os valor da array, um por um: (digite TERMINAr para sair")
	n = int(m)
	j = 1 # j
	
	u1 = (j*pi/n+1)
	
	
	
	
		
	lamb_j = 2*(1 - coseno(u1)) #var lambdaJ
	print("lambda jota")
	print(lamb_j)
		
	while(j<=4):
		u2 = (n*j*pi/n+1)
		vj = seno(u2) #autovalores correspondentes
		print("Para j = " + str(j))
		print("vj:")
		print(vj)
			
		
		j = j+1
		
		

	return lamb_j*vj

#print(lambda_j())

#def I():
#	np.array.identity(3, dtype=float)
#	array([[ 1.,  0.,  0.],
#	       [ 0.,  1.,  0.],
#	       [ 0.,  0.,  1.]])
#	return identity


def questaoA():
	k = 0
	Q = np.array([coseno(pi)])
	
	#A = lambda_j()
	#R = Q*Q*A
	

	A = ((Q*Q*lambda_j())**(k))*(Q**(k)) +uk*np.eye(3)
	print("Questão A")
	print(A**(k+1))
	

print(questaoA())

