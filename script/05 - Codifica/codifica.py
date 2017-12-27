def Sort(As, C):
	l = len(As)
	for i in range(l-1, -1, -1):
		for j in range(i):
			if C(As[j], As[j+1]):
				As[j], As[j+1] = As[j+1], As[j]

def ComputeTable(s):
	char2int, int2char, count = {}, {}, 0
	for c in s:
		if not c in char2int:
			count += 1
			char2int[c] = count
			int2char[count] = c
	return char2int, int2char


def SortFreqences(As):
	#As sono frequenze nella forma [lettera, frequenza]
	return Sort(As, lambda x, y: x[1]<y[1])

def PulisciTesto(s, blanks):
	r = s[:]
	for c in blanks:
		r = r.replace(c,'')
	return r

def PulisciTestoASCII(s, nospace=True):
	for i in range(126):
		if (i < 48 or (i > 57 and i < 65) or (i > 90 and i < 97) or (i > 122)):
			if nospace or i != 32:
				s = s.replace(chr(i), '')
	return s

def ContaCaratteri(s):    
	D = {}          # Costruttore di un dizionario vuoto
	for c in s:     # Ciclo su tutti caratteri della stringa
		if c in D:
			D[c] += 1
		else:
			D[c] = 1
	return D

def CalcolaFrequenza(D):
	F = {}
	count = 0
	for key in D:
		count += D[key]
	for key in D:
		F[key] = D[key]/count * 100
	return F

def StampaDizionario(D):
	for key in D:
		print (key,D[key],sep=' --> ')

def AnalisiTesto(path):
	fh = open(path, 'r', encoding="utf-8")
	s = fh.read()
	fh.close()
	s = PulisciTestoASCII(s)
	s = PulisciTesto(s, ' “—«„   »').lower()
	D = ContaCaratteri(s.replace("'","").lower())
	if path == 'LeAvventureDiPinocchio.txt':
		for key in D:
			if D[key] < 2:
				a = key
		del D[a]
	F = CalcolaFrequenza(D)
	
	return D, F

def Encode(text, dic):
	code = ''
	for c in text:
		if c in dic:
			code += dic[c]
		else:
			code += c
	return code

def invert(dic):
	inv = {}
	for i in dic:
		inv[dic[i]] = i
	return inv

def dic2list(dic):
	l = []
	for i in dic:
		l.append((i, dic[i]))
	return l

def list2dic(l):
	d = {}
	for i in l:
		d[i[0]] = i[1]
	return d

def sortF(F):
	fList = dic2list(F)
	SortFreqences(fList)
	F = list2dic(fList)
	return F



