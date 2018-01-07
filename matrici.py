from sympy import Matrix, Symbol, solve, eye, zeros, pprint, init_printing, factor
from sympy.parsing.sympy_parser import parse_expr
import os

class AppLin():
	def __init__(b1, b2, M):
		self.b1 = b1
		self.b2 = b2
		self.M = M

x = Symbol('x')
t = Symbol('t')

def GetMatrix(r, c):
	B = []
	for i in range(c):
		print('\nVettore ',i+1)
		B.append(GetVector(r))	
	
	return Matrix(B).T

def GetVector(d):
	a = []
	while len(a) != d:
		a = input('Inserisci le '+str(d)+' componenti separate da uno spazio: ')
		a = a.strip().split(' ')
	
	b = [parse_expr(i) for i in a]
	return b

def SolveAppLin():
	CS()
	#Base di partenza
	d1 = input('Inserisci la dimensione di partenza:\neN per la base std\n')
	if d1[0] == 'e':
		d1 = d1[1:]
		b1 = eye(int(d1))
	else:
		b1 = GetMatrix(int(d1), int(d1))
		
	
	#Base di arrivo
	d2 = input('Inserisci la dimensione di arrivo:\neN per la base std\n')
	if d2[0] == 'e':
		d2 = d2[1:]
		b2 = eye(int(d2))
	else:
		b2 = GetMatrix(int(d2), int(d2))
		
	#App. Lin.
	print('Inserisci le componenti dell\'applicazione lineare: ')
	app = GetMatrix(int(d2), int(d1))
	
	#Base di partenza richiesta
	d3 = input('Inserisci la dimensione di partenza richiesta: \neN per la base std\nb1 per la base di parteza data\nb2 per la base di arrivo data\n')
	if d3[0] == 'e':
		d3 = d3[1:]
		b3 = eye(int(d3))
	elif d3 == 'b1':
		d3 = d1
		b3 = b1
	elif d3 == 'b2':
		d3 = d2
		b3 = b2
	else:
		b3 = GetMatrix(int(d3), int(d3))
	
	#Base di arrivo richiesta
	d4 = input('Inserisci la dimensione di arrivo richiesta: \neN per la base std\nb1 per la base di parteza data\nb2 per la base di arrivo data\nb3 per la base di partenza richiesta\n')
	if d4[0] == 'e':
		d4 = d4[1:]
		b4 = eye(int(d4))
	elif d4 == 'b1':
		d4 = d1
		b4 = b1
	elif d4 == 'b2':
		d4 = d2
		b4 = b2
	elif d4 == 'b3':
		d4 = d3
		b4 = b3
	else:
		b4 = GetMatrix(int(d4), int(d4))
		
	T = (b4**-1)*b2*app*(b1**-1)*b3
	
	CS()
	
	pprint(T)
	print('\n\n')
	c = input('Polinomio caratteristico? y\\N ') 
	if c == 'y':
		x = Symbol('x')
		p = T.charpoly(x)
		pprint(p)
		print('\n\n')
	c = input('Autovalori? y\\N ')
	if c == 'y':
		pprint(T.eigenvals())
		print('\n\n')
	c = input('Autovettori? y\\N ')
	if c == 'y':
		pprint(T.eigenvects())

def CS():
	#Da sistemare
	os.system('clear')
	
t = Symbol('t')
A = Matrix([[t-1, 0, 0, 0],[2*t, 1, 0, -1], [0, 2*t, 2*t-1, t],[3*t, 1, 0, 2*t-3]])


print("T = 0")
pprint(A.subs(t, 0).eigenvects())
print("T = 3")
pprint(A.subs(t, 3).eigenvects())
print("T = 1")
pprint(A.subs(t, 1).eigenvects())
print("T = 3/4")
pprint(A.subs(t, 3/4).eigenvects())

#print(A.det())


if __name__ == '__main__' and 0:
	gAppLin = 0
	
	
	
	print ('Algebra Lineare\n\n')
	
	while True:
		print('Inserisci l\'azione da compiere (-1 per terminare): ')
		print('1 --> Nuova Applicazione Lineare')
		
		
		try:
			a = int(input())
			if a == 1:
				SolveAppLin()
			elif a == -1:
				break
			else:
				CS()
				print ('Numero non riconosciuto!! \n\n')
		
		except ValueError:
			CS()
			print ('Inserisci solo numeri!! \n\n')
		
		
		
		#print (Format(a))
		#print (A.eigenvals())
		#pprint (A)
		#pprint (B.eigenvects())
		#print (D.nullspace())
