def monete(x, L):
	if x == 0:
		return 1
	if len(L) == 1:
		if x % L[0] == 0:
			return 1
		return 0
	if L[0] > x:
		return monete(x, L[1:])
	return monete(x-L[0], L) + monete(x, L[1:])

print (monete(20, [10,5,2,1]))
print (monete(100, [50,20,10,5,2,1]))
