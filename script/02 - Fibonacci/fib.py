
def FibR(n):
	#ricorsivo
	#O(exp)
	if n == 0 or n == 1:
		return n
	return FibR(n-1) + FibR(n-2)

def FibI(n, H = 1, L = 0):
	#iterativo
	#O(n)
	global count
	count = count +1
	if n == 0:
		return L
	if n == 1:
		return H
	return FibI(n-1, H+L, H)


def FibLog(a, b = -1):
	if b == -1:
		#prima chiamata
		if a%2 == 0:
			return FibLog(a-1, a)[1]
		return FibLog(a, a+1)[0]
	
	if a < 2 and b < 2:
		return a, b
	
	if a%2 == 0:
		A, B = FibLog(int(a/2-1), int(a/2))
	else:
		A, B = FibLog(int(b/2-1), int(b/2))
	
	C = A**2 + B**2
	D = B*(2*A + B)
	
	if a%2 == 0:
		return D, C+D
	return C, D
	


print (FibLog(10000))





"""

1*F(8) + 0*F(7)
	(1+0)= 1*F(7) + 1*F(6)
		(1+1)= 2*F(6) + 1*F(5)
			(2+1)= 3*F(5) + 2*F(4)
				(3+2)= 5*F(4) + 3*F(3)

F(1)*F(8) + F(0)*F(7)
	F(2)*F(7) + F(1)*F(6)
		F(3)*F(6) + F(2)*F(5)
-->			F(4)*F(5) + F(3)*F(4)
				F(5)*F(4) + F(4)*F(3)

F(1)*F(9) + F(0)*F(8)
	F(2)*F(8) + F(1)*F(7)
		F(3)*F(7) + F(2)*F(6)
			F(4)*F(6) + F(3)*F(5)
-->				F(5)*F(5) + F(4)*F(4)




"""
