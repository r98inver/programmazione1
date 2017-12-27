
"""
Liste costruite come sequenza di numeri complessi
"""


# -*- coding: utf-8 -*-

def EmptyList():
    """ Simbolo usato per indicare una lista vuota """
    return 0

def MakeList(x, y=[]):
    """ Restituisce una lista come sequenza di coppie """
    if y == []:
        return [x] 
    return [x] + y

def Head(As):
    """ Restituisce il primo elemento della lista As """
    return As[0]

def Tail(As):
    """ Restituisce il secondo elemento della lista As """
    return As[1:]
    
