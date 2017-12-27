import matplotlib.pyplot as plt
import numpy as np

def DrawMatrix(m, N):
    fig = plt.figure(figsize=(N,N))
    img = plt.imshow(m, cmap='gray')
    plt.show()    

def VoidMatrix(n):
	return [[0 for i in range(n)] for j in range(n)]

def List2Matrix(P):
	M = VoidMatrix(len(P))
	for x in range(len(P)):
		M[x][P[x]] = 1
	return M



def Pos2Matrix(P):
	M = VoidMatrix(len(P))
	for pos in P:
		M[(int)(pos.real)][(int)(pos.imag)] = 1
	return M

def FuoriCampo(p, N):
	if p.real >= N or p.imag >= N:
		return True
	return False

def Scacco(p1, p2):
	d1 = p1.real - p2.real
	d2 = p1.imag - p2.imag
	
	if d1 == 0 or d2 == 0 or abs(d1) == abs(d2):
		return True
	
	return False

def Libero(pos, R):
	for r in R:
		if Scacco(r, pos):
			return False
	return True
