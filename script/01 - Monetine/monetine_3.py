import time

def monetine(tot, l, x=0, low=0):
	if x > tot:
		return 0
	if x == tot:
		return 1
		
		
	ris = 0
	
	for i in l:
		if low <= i:
			ris = ris + monetine(tot, l, x+i, i)
	
	return ris


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
	print( monetine(b, a))
	print (time.clock() - start_time, "seconds")

main()
