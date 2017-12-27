# -*- coding: utf-8 -*-
"""
Libreria per la gestione di liste create usando una catena di coppie

@author: gualandi
"""

#from pairslist_impl import Head, Tail, EmptyList, MakeList
from pairslist_array import Head, Tail, EmptyList, MakeList

from random import randint

# Inizializza il generatore di numeri casuali
# Vedi la documentazione del modulo random:
# https://docs.python.org/3/library/random.html
def MakeRandomInts(n, a, b):
	""" Restituisce una lista n di numeri causali, uniformente distribuiti
		nell'intervallo [a,b] (estremi compresi) """
	if n == 0:
		return EmptyList()
	return MakeList(randint(a,b), MakeRandomInts(n-1, a, b))


def PrintList(As):
	""" Pretty print for a list of elements """
	def PrintListI(As):
		if not IsEmpty(As):
			print(Head(As), end='')
			if not IsEmpty(Tail(As)):            
				print(', ', end='')
			PrintListI(Tail(As))
	print('{', end='')
	PrintListI(As)
	print('}')    

def IsEmpty(As):
	""" Controlla se As è una lista vuota """
	return As == EmptyList()

def MakeRange(a, b):
	""" Restituisce la lista di numeri interi compresi tra 1 e n """
	def MakeI(n):
		if n > b:
			return EmptyList()
		return MakeList(n, MakeI(n+1)) 

	if b < 1:
		print("RuntimeError: Il numero n deve essere maggiore o uguale a 1")
		return EmptyList

	return MakeI(a)

def Nth(As, i):
	""" Restituisce l'i-esimo elemento della lista As """
	if IsEmpty(As):
		return As
	if i == 0:
		return Head(As)
	return Nth(Tail(As), i-1)

def Equal(As, Bs):
	""" Check if two lists have the same sequence of elements """
	if IsEmpty(As) and IsEmpty(Bs):
		return True
	if IsEmpty(As) and not IsEmpty(Bs):
		return False
	if not IsEmpty(As) and IsEmpty(Bs):
		return False
	if Head(As) != Head(Bs):
		return False
	return Equal(Tail(As), Tail(Bs))
	
def Length(As):
	""" Restituisce il numero di elementi contenuto nella lista As """
	def LengthI(Ls, n):
		if IsEmpty(Ls):
			return n
		return LengthI(Tail(Ls), n+1)
	return LengthI(As, 0)

def Append(As, Bs):
	""" Aggiungi la lista Bs in coda alla lista As """
	if IsEmpty(As):
		return Bs
	return MakeList(Head(As), Append(Tail(As), Bs))

def Scala(As, a):
	""" Restituisci una nuova lista che per ogni elemento di As
		contiene lo stesso valore moltiplicato per 'a' """
	if IsEmpty(As):
		return As
	return MakeList(a*Head(As), Scala(Tail(As), a))

def Quadrati(As):
	""" Restituisci una nuova lista che per ogni elemento di As
		contiene lo stesso valore al quadrato """
	if IsEmpty(As):
		return As
	return MakeList(Head(As)*Head(As), Quadrati(Tail(As)))
	
def Map(F, As):
	""" Restituisci una nuova lista che per ogni elemento di As
		contiene il valore ottenuto applicato F() ad all'elemento """
	if IsEmpty(As):
		return As
	return MakeList(F(Head(As)), Map(F, Tail(As)))

def Filter(P, As):
	""" Restituisci una nuova lista che contiene solo gli elementi di As
		che soddisfano il predicato P() """
	if IsEmpty(As):
		return As
	if P(Head(As)):
		return MakeList(Head(As), Filter(P, Tail(As)))
	return Filter(P, Tail(As))
		
def Reverse(As):
	""" Restituisci una nuova lista gli elemento di As in ordine inverso """
	def ReverseI(Ls, Rs):
		if IsEmpty(Tail(Ls)):
			return MakeList(Head(Ls), Rs)
		return ReverseI(Tail(Ls), MakeList(Head(Ls), Rs))
	return ReverseI(Tail(As), MakeList(Head(As)))

def Contains(As, value):
	""" Controlla se la lista As contiene un elemento pari a 'value' """
	if IsEmpty(As):
		return False
	if Head(As) == value:
		return True
	return Contains(Tail(As), value)

def Count(As, value):
	""" Conta il numero di elementi pari a 'value' nella lista As """
	def CountI(Ls, counter):
		if IsEmpty(Ls):
			return counter
		if Head(Ls) == value:
			return CountI(Tail(Ls), counter+1)
		return CountI(Tail(Ls), counter)
	
	return CountI(As, 0)

def RemoveFirst(As, value):
	""" Rimuovi il primo elemento di 'value' trovato in As """
	if IsEmpty(As):
		return As
	if Head(As) == value:
		return Tail(As)
	return MakeList(Head(As), RemoveFirst(Tail(As), value))

def RemoveAll(As, value):
	""" Rimuovi tutti gli elementi di 'value' trovato in As """
	if IsEmpty(As):
		return As
	if Head(As) == value:
		return RemoveAll(Tail(As), value)
	return MakeList(Head(As), RemoveAll(Tail(As), value))

def FoldRight(Op, As, z):
	""" Riduci la lista As, applicando ad ogni suo elemento la funzione F()
		e accumulando i risultati tramite l'operazione Op() """
	if IsEmpty(As):
		return z
	return Op(Head(As), FoldRight(Op, Tail(As), z))

def FoldLeft(Op, As, z):
	if IsEmpty(As):
		return z
	return FoldLeft(Op, Tail(As), Op(Head(As), z))
	
Fold = FoldLeft

# SOLUZIONI IN TERMINI DI FOLD (Right)

def FoldLength(Ls):
	""" Lunghezza di una lista in termini di fold """
	return Fold(lambda x,y: 1+y, Ls, 0)

def Sum(As):
	""" Calcola la somma di tutti gli elementi nella lista As """
	def Add(a, b):
		return a+b
	return Fold(Add, As, 0)

def Prod(As):
	""" Calcola la somma di tutti gli elementi nella lista As """
	def Mul(a, b):
		return a*b
	return Fold(Mul, As, 1)

def Min(As):
	""" Più piccolo elemento della lista As """
	return Fold(min, Tail(As), Head(As))

def Max(As):
	""" Più grande elemento della lista As """
	return Fold(max, Tail(As), Head(As))

def FoldMap(F, Ls):
	""" Map in termini di Fold """
	return Fold(lambda x,y: MakeList(F(x), y), Ls, EmptyList())

def FoldFilter(P, Ls):
	""" Filter in termini di Fold """
	return Fold(lambda x,y: MakeList(x, y) if P(x) else y, Ls, EmptyList())

def FoldReverse(Ls):
	""" Reverse in termini di Fold """
	def Concatenate(x, Ls):
		return Append(Ls, MakeList(x))
	return Fold(Concatenate, Ls, EmptyList())  

def SplitList(Ls, end, start=0):
	""" Ritorna gli elementi da start a end-1"""
	if start >= end:
		return EmptyList()
	return MakeList(Nth(Ls, start), SplitList(Ls, end, start+1))

def HalfList(Ls):
	""" Ritorna le due metà di una lista """
	l = Length(Ls)
	if l < 2:
		return Ls, []
	return SplitList(Ls, int(l/2)), SplitList(Ls, l, int(l/2))
