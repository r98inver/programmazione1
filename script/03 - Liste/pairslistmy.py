# -*- coding: utf-8 -*-
"""
Libreria per la gestione di liste create usando una catena di coppie

@author: r98inver
"""

def MakeRange(a, b):
	"""Costruisce una lista di numeri da a a b"""
	if a == b:
		return (a, None)
	return (a, MakeRange(a+1, b))

def IsEmpty(a):
	return a == None

def MakeList(n):
    """ Restituisce la lista di numeri interi compresi tra 1 e n """
    return MakeRange(1, abs(int(n)))

def Head(As):
    """ Restituisce il primo elemento della lista As """
    return As[0]

def Tail(As):
    """ Restituisce il secondo elemento della lista As """
    return As[1]

def Nth(As, i):
    """ Restituisce l'i-esimo elemento della lista As """
    if i == 0:
        return Head(As)
    return Nth(Tail(As), i-1)

def Length(As):
    """ Restituisce il numero di elementi contenuto nella lista As """
    def LengthI(As, x):
        if As == None:
            return x
        return LengthI(Tail(As), x+1)
    return LengthI(As, 0)
    
def Append(As, Bs):
	"""Concatena due liste"""
	if As[1] == None:
		return (As[0], Bs)
	return (As[0], Append(As[1], Bs))

def Map(F, As):
	"""Applica una funzione ad ogni elemento della lista"""
	if As == None:
		return None
	return (F(Head(As)), Map(F, Tail(As)))

def Scala(As, a):
	"""Moltiplica ogni elemento della lista per a"""
	return Map(lambda x: a*x, As)
	

def Quadrati(As):
	"""Eleva ogni elemento della lista al quadrato"""
	return Map(lambda x: x*x, As)

def Filter(P, As):
	"""Filtra la lista secondo un predicato P"""
	if As == None:
		return None
	if P(As[0]):
		return (As[0], Filter(P, As[1]))
	return Filter(P, As[1])
    
def Reverse(As, B = None):
	"""Ritorna la lista invertita"""
	if As[1] == None:
		return (As[0], B)
	return Reverse(As[1], (As[0], B))

def Accumula(Op, As, V):
	if As == None:
		return V
	return Op(Head(As), Accumula(Op, Tail(As), V))

def Contains(As, v):
	if IsEmpty(As):
		return 0
	return Head(As) == v or Contains(Tail(As), v)

def FoldRight(P, As, v):
	if IsEmpty(As):
		return v
	return P(Head(As), FoldRight(P, Tail(As), v))
	
def Reverse(As):
	return Tail( (FoldRight(lambda x, y: (y,x), As, None), None ))

#-----------------------------------------------
# MAIN function per testare tutte le soluzioni
#-----------------------------------------------

if __name__ == "__main__":
	def F():
		return lambda x,y: x if x > y else y
		
	print (F()(3,4))
	#print ('ciao')
	Ls = MakeList(7)
	print (Reverse(Ls))
