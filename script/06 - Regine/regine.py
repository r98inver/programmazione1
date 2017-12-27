from helper import *

"""Struttura dati: lista di numeri/indici che danno la posizione"""

def Check(P):
	"""
	Controllo di una generica soluzione
	Complessità: O( N^2 + 2N ) => O(N^2)
	"""
	dim = len(P) #O(N)
	
	for x in range(dim):
		for y in range(x+1, dim):
			if P[x] == P[y] or abs(x-y) == abs(P[x]-P[y]):
				return False #O(2N(N+1)/2)
	return True

def SolveRec(P, N, D, S):
	
	#Se sono riuscito a generare una lista di lunghezza N il problema è risolto
	if len(P) == N:
		return P
	
	#Non ho problemi con le colonne (indici di P)
	for i in range(N):
		
		if i in P:
			#Se la riga i è già usata passo al numero successivo
			continue
		
		Di = i + len(P) #la diagonale 'destra' della posizione
		Si = i - len(P) + N #la diagonale 'sinistra della posizione (+N per avere indici positivi)
		
		if D[Di] == 1 or S[Si] == 1:
			continue
		
		#La regina non è sotto scacco
		D[Di] = 1
		S[Si] = 1
		ris = SolveRec(P+[i], N, D, S)
		
		if not ris:
			D[Di] = 0
			S[Si] = 0
			continue
		
		return ris
	return False

def Conta(P, N, D, S):
	if len(P) == N:
		return 1
	
	count = 0
	for i in range(N):
		#if len(P) == 2:
		#	print ('Sezione ',P[0],'.',P[1],'.',i,sep='')
		if i in P:
			continue
		Di = i + len(P)
		Si = i - len(P) + N
		if D[Di] == 1 or S[Si] == 1:
			continue
		D[Di] = 1
		S[Si] = 1
		count += Conta(P+[i], N, D, S)
		D[Di] = 0
		S[Si] = 0
		
	return count
	


def Solve(N, c=0):
	D, S = [0]*2*N, [0]*2*N
	
	if c == 0:
		P = SolveRec([], N, D, S)
		
		if not P:
			print ('Nessuna soluzione trovata')
		
		else:
			M = List2Matrix(P)
			print (P)
			print (M)
			DrawMatrix(M, N)
		
	else:
		C = Conta([], N, D, S)
		print (C)
	
	return 0
	
def main():
	a = int(input('Inserisci la dimensione: '))
	b = int(input("Inserisci l'azione da compiere: \n 0 --> Risolvi \n 1 --> Conta soluzioni \n"))
	Solve(a, b)

if __name__ == "__main__":
	main()
