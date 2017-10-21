import time

count = 0


def stampa(a, l):
	for i in range(len(a)):
		if a[i] != 0:
			print (a[i], 'monete da', l[i])
	print ('')

def scala(l):
	
	for i in range(len(l)):
		if l[i] != 0:
			if i == len(l)-1:
				return False
			l[i] = 0
			l[i+1] = l[i+1] + 1
			return True

def checkList(val, l, a):
	x = 0
	for i in range(len(a)):
		x = x + a[i] * l[i]
		
		if x < val:
			continue
		
		if x == val:
			global count
			count = count + 1
			#stampa (a, l)
		
		if scala(a):
			return checkList(val, l, a)
		
		return False
	
	return a
	
def monetineBF(val, l):
	
	p = len(l)
	l.sort()
	a = [0] * p

	while a:
		a[0] = a[0] + 1
		a = checkList(val, l, a)
	
	global count
	print (count,'combinazioni possibili')
	
	
def main():
	a = []
	b = 0
	while b != -1:
		if b != 0:
			a = a + [b]
		try:
			b = int(input(('Inserisci una alla volta le monete disponibili in cent.(-1 per finire): ')))
		except:
			b = 0
			print ('Inserire solo numeri!')

	b = int(input(('Inserisci il resto(in cent.): ')))
	start_time = time.clock()
	print( monetineBF(b, a))
	print (time.clock() - start_time, "seconds")
	


main()
