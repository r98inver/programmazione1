def isPrime(n, a = 2):
	if n < 2:
		return False
	if a**2 > n:
		return True
	return False if n%a == 0 else isPrime(n, a+1+a%2)
	
	
def MCD(a, b):
	if b > a:
		return MCD(b, a)
	if b == 0:
		return a
	return MCD(b, a%b)


def Palindromo(S):
    for i in range(len(S)):
        if i >= len(S)-i:
            return True
        if S[i] != S[-i-1]:
            return False
