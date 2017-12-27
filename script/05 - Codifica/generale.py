from codifica import *

_data = 'LeAvventureDiPinocchio.txt'
P = 'testo_segreto_difficile.txt'
words = []

testo_in_chiaro = """
— No, no, no e poi no. Oramai ho promesso alla mia buona Fata di
diventare un ragazzo perbene, e voglio mantenere la promessa. Anzi,
siccome vedo che il sole va sotto, cosè ti lascio subito e scappo via.
Dunque addio, e buon viaggio.
"""



def SetWords():
	fh = open(_data, 'r', encoding="utf-8")
	s = fh.read()
	fh.close()
	
	s = PulisciTesto(s, '“—«„»,.').lower()
	s = PulisciTesto(s,"'")
	s = PulisciTestoASCII(s, nospace = False)
	global words 
	for t in s.split(' '):
		if len(t) > 0:
			words.append(t)

def TrovaVocali(text):
	#trova a, e, i, o come le ultime lettere delle parole
	vocali = []
	for t in text:
		if len(t[0]) > 2:
			vocali.append(t[0][-1])
	
	vocali = CalcolaFrequenza(ContaCaratteri(vocali))
	vocali = dic2list(vocali)
	SortFreqences(vocali)
	v = []
	for t in range(4):
		v.append(vocali[t][0])
	return v


def AggiornaTesto(text, old, new):
	for t in text:
		for i in range(len(t[0])):
			if t[0][i] == old:
				t[1] = t[1][:i] + new + t[1][i+1:]
	
def ControllaTesto(encoded_text):
	#Stati
	#	-1 --> Il testo è sbagliato
	#	0 --> Testo senza errori
	#	1 --> Testo completamente codificato corretto
	global words

	uncheck = False
	for t in encoded_text:
		if '*' in t[1]:
			uncheck = True
		elif not t[1] in words:
			#print ('error: ',t[1])
			return -1
	
	if uncheck:
		return 0
	return 1


def BFDecode(all_decode, text, already_used = ''):
	
	#prendo il primo valore
	A = all_decode[0]
	
	for a in A[1]:
		if a in already_used:
			#la lettera con cui decodificare è già usata
			continue
			
		#Inserisce la nuova lettera nel testo e controlla il testo
		AggiornaTesto(text, A[0], a)
		status = ControllaTesto(text)
		
		if status == -1:
			#Il testo contiene già parole non esistenti
			AggiornaTesto(text, A[0], '*')
			continue
		
		if status == 1 or len(all_decode) == 1:
			#Il testo è completamente corretto
			return text
		next_encode = BFDecode(all_decode[1:], text, already_used+a)
		if next_encode != False:
			return next_encode
		AggiornaTesto(text, A[0], '*')
	
	#se non ho trovato un testo funzionante ritorno un errore
	return False
	
def main():
	
	decode = {}
	
	fh = open(P, 'r', encoding="utf-8")
	s = fh.read()
	fh.close()
	s = PulisciTesto(s, '“—«„»,.').lower()
	s = s.split(' ')
	
	encoded_text = []
	for t in s:
		x = len(t)
		if x > 0:
			encoded_text.append([t, x*'*'])
	
	#le prime 4 sono vocali
	vocali = TrovaVocali(encoded_text)
	
	
	#trovo la e come quella che sta più da sola (51% circa)
	e = []
	
	for t in encoded_text:
		if len(t[0]) == 1:
			e.append(t[0])
	
	e = CalcolaFrequenza(ContaCaratteri(e))
	e = dic2list(e)
	SortFreqences(e)
	e = e[0][0]
	decode[e] = 'e'
	vocali.remove(e)
	AggiornaTesto(encoded_text, e, 'e')
		
	#ho le vocali [a, i, o] che possono andare solo nei tre valori di vocali
	
	found = vocali + [e]
	text = ''
	for t in s:
		for c in t:
			if not c in found:
				text += c
	
	d = ContaCaratteri(text)
	f = CalcolaFrequenza(d)
	
	fh = open(_data, 'r', encoding="utf-8")
	s = fh.read()
	fh.close()
	
	s = PulisciTesto(s, '“—«„»,.').lower()
	s = PulisciTesto(s,"'")
	s = PulisciTestoASCII(s)
	found = ['a', 'i', 'o', 'e']
	for i in found:
		s = PulisciTesto(s, i)
	D = ContaCaratteri(s)
	F = CalcolaFrequenza(D)

	F = sortF(F)
	f = sortF(f)
	
	error = 0.5
	
	all_decode = {}
	
	for i in vocali:
		all_decode[i] = ['a', 'i', 'o']
	
	countf = 0
	for char in f:
		countF = 0
		l = []
		for code in F:
			if (F[code] > f[char]*(1-error) and F[code] < f[char]*(1+error)) or (abs(countf - countF) < 4):
				l += [code]
			countF += 1
		all_decode[char] = l
		countf += 1
		
	SetWords()
	
	all_decode = dic2list(all_decode)
	
	
	"""all_decode_correct = [
	('a', ['n']), 
	('b', ['o']), 
	('c', ['r']), 
	('e', ['f']), 
	('g', ['u']), 
	('h', ['g']), 
	('j', ['m']), 
	('l', ['s']), 
	('m', ['t']), 
	('o', ['z']), 
	('p', ['c']), 
	('q', ['l']), 
	('r', ['v']), 
	('s', ['d']), 
	('t', ['b']), 
	('u', ['q']), 
	('v', ['p']), 
	('w', ['i']), 
	('x', ['h']), 
	('y', ['ì']), 
	('z', ['a']), ]"""
	
	decoded_text = BFDecode(all_decode, encoded_text)
	for i in decoded_text:
		for t in range(len(i[0])):
			if not i[0][t] in decode:
				decode[i[0][t]] = i[1][t]
	
	StampaDizionario(decode)
	
	
	fh = open(P, 'r', encoding="utf-8")
	s = fh.read()
	fh.close()
	
	testo_in_chiaro = Encode(s, decode)
	print (testo_in_chiaro)
	

if __name__ == "__main__":
	main()
