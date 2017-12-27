
def IsSet(As, P=lambda x,y: x==y):
	N = len(As)
	for x in range(N):
		for y in range(x+1, N):
			if P(As[x], As[y]):
				return False
	return True


print (IsSet([1,2,3,4,6,7,4]))
