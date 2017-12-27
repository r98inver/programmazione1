# -*- coding: utf-8 -*-
"""
Libreria per l'ordinamento delle liste
"""
from pairslist import *

def Merge(Ls1, Ls2, P):
	
	if Ls1 == EmptyList():
		return Ls2
	
	if Ls2 == EmptyList():
		return Ls1
	
	#Le liste sono certamente ordinate quindi il primo elemento è il primo da controllare
	a = Head(Ls1)
	b = Head(Ls2)
	
	if P(a, b):
		return MakeList(a, Merge(Tail(Ls1), Ls2, P))
	
	return MakeList(b, Merge(Ls1, Tail(Ls2), P))

def MergeSort(Ls, P = (lambda x,y: x > y)):
	
	if Length(Ls) < 2:
		#Una lista che contiene uno o nessun elemento è certamente ordinata
		return Ls
	
	#Le due metà della lista
	l1, l2 = HalfList(Ls)
	
	#Prima metà della lista ordinata
	Ls1 = MergeSort(l1, P)
	
	#Seconda metà della lista ordinata
	Ls2 = MergeSort(l2, P)
	
	#Fa il Merge delle due liste secondo la proposizione P e ritorna una lista ordinata
	OLs = Merge(Ls1, Ls2, P)

	return OLs


Ls = MakeRandomInts(100, 1, 10000)
print (MergeSort(Ls, lambda x,y: x < y))


