def isPrime(n, a=2):
	if n == 1:
		return False
	if n == 2:
		return True
	if n % a == 0:
		return False
	if a**2 > n:
		return True
	return isPrime(n, a+1)
	
def MCD(a, b):
	if b > a:
		return MCD(b, a)
	if b == 0:
		return a
	return MCD(b, a%b)

def FiltraAccumula(P, Op, E, F, a, Next, b):
	print (a, E)
	if a > b:
		return E
	return FiltraAccumula(P, Op, Op(E, F(a)) if P(a) else E, F, Next(a), Next, b)
	
def FiltrAccR(P, Op, E, F, a, Next, b):
	if a > b: 
		return E
	return Op(F(a) if P(a) else E, FiltrAccR(P, Op, E, F, Next(a), Next, b))

def Accumula(Op, E, F, a, Next, b):
	return FiltraAccumula(lambda x: True, Op, E, F, a, Next, b)

def Sommatoria(F, a, Next, b):
	return Accumula(lambda x,y: x+y, 0, F, a, Next, b)

def Produttoria(F, a, Next, b):
	return Accumula(lambda x,y: x*y, 1, F, a, Next, b)

def sqrPrime(a, b):
	return FiltraAccumula(isPrime, lambda x, y: x+y, 0, lambda x: x**2, a, lambda x: x+1, b)

def coPrime(n):
	return FiltraAccumula(lambda x: MCD(n, x) == 1, lambda x, y: x*y, 1, lambda x: x, 1, lambda x: x+1, n)


