def TestZero ():
	if Intersect ((2 ,3 ,4 ,2 ,1 ,2 ,7) , (2 ,3 ,2 ,3 ,4)) == (2, 3, 4):
		return 'ok'
	return 'failed'
	

def Intersect(a, b):
	c = ()
	for i in a:
		if i in b and not i in c:
			c = c + (i,)
	return c

def RimuoviDuplicati(a, b):
	for i in b:
		for t in range(a.count(i)):
			a.remove(i)

