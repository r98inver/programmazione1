from codifica import *

_data = 'LeAvventureDiPinocchio.txt'
P = 'testo_segreto_difficile.txt'




def TrovaVocali(text):
	#trova a, e, i, o come le ultime lettere delle parole
	vocali = []
	for t in text:
		if len(t[0]) > 2:
			vocali.append(t[0][-1])
	
	vocali = CalcolaFrequenza(ContaCaratteri(vocali))
	vocali = dic2list(vocali)
	SortFreqences(vocali)
	return vocali


def matchCode(sText, sCode, decode):
	for i in range(len(sText)):
		isIn = False
		for t in decode[sCode[i]]:
			if t[0] == sText[i]:
				isIn = True
		if not isIn:
			return False
	return True

def associa(text, code, decode):
	for c in code:
		for t in text:
			if matchCode(t, c, decode):
				newF = text[t] * code[c] / 100
				for i in range(len(t)):
					for j in decode[c[i]]:
						if j[0] == t[i]:
							j[1] += newF
	return decode
				
	

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
	vocali = TrovaVocali(encoded_text)[0:4]
	
	#trovo la e come quella che sta più da sola (51% circa)
	
	
	
	
	StampaDizionario (decode)
	exit()
	
	
	
	D, F = AnalisiTesto(_data)
	F = sortF(F)
	#StampaDizionario(F)
	
	d, f = AnalisiTesto(P)
	f = sortF(f)
	#StampaDizionario(f)
	
	Keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'à', 'è', 'ì', 'ò', 'ù']
	char2int, int2char = ComputeTable(Keys)
	
	#Definisco un margine nella ricerca delle frequenze
	#Su questo punto sono andato per tentativi ma immagino esista una 
	#soluzione migliore
	error = 0.35
	
	
	#Associo ad ogni lettera quelle più vicine a lei
	decode = {}
	nchar = len(Keys)
	
	
	countf = 0
	for char in f:
		countF = 0
		l = []
		for code in F:
			if (F[code] > f[char]*(1-error) and F[code] < f[char]*(1+error)) or (abs(countf - countF) < 2):
				l += [code]
			countF += 1
		decode[char] = l
		countf += 1
	
	#Trovo la frequenza nel testo e nel codice di parole da una, due e tre lettere
	fh = open(P, 'r', encoding="utf-8")
	s = fh.read()
	fh.close()
	s = PulisciTesto(s, '“—«„»,.').lower()
	s = s.split(' ')
	code1, code2, code3 = [], [], []
	for t in s:
		if(len(t)) == 1:
			code1.append(t)
		if(len(t)) == 2:
			code2.append(t)
		if(len(t)) == 3:
			code3.append(t)
	code1 = CalcolaFrequenza(ContaCaratteri(code1))
	code2 = CalcolaFrequenza(ContaCaratteri(code2))
	code3 = CalcolaFrequenza(ContaCaratteri(code3))
	
	
	fh = open(_data, 'r', encoding="utf-8")
	s = fh.read()
	fh.close()
	s = PulisciTesto(s, '“—«„»,.').lower()
	s = PulisciTestoASCII(s, nospace=False)
	s = s.split(' ')
	text1, text2, text3 = [], [], []
	for t in s:
		if(len(t)) == 1:
			text1.append(t)
		if(len(t)) == 2:
			text2.append(t)
		if(len(t)) == 3:
			text3.append(t)
	text1 = CalcolaFrequenza(ContaCaratteri(text1))
	text2 = CalcolaFrequenza(ContaCaratteri(text2))
	text3 = CalcolaFrequenza(ContaCaratteri(text3))
	
	#Controllo la compatibilità di queste parole con quelle contenute
	#nel codice
	#1 lettera --> ogni parola da una lettera contenuta nel codice
	#	guadagna tutte le frequenze delle parole da 1 lettera contenute
	#	nel testo
	#	es: k -> (e, f, d), k compare una volta nel testo => k -> (e=0.123, f, g)
	#2, 3 lettere --> stesso ragionamento ma con coppie o terne di lettere
	#	es: nel codice compare un ker
	#		se k -> d, e -> a, r -> i, => k[d], e[a], r[i] guadagnano la
	#		frequenza di dai nel testo
	
	decode = associa(text1, code1, decode)
	decode = associa(text2, code2, decode)
	decode = associa(text3, code3, decode)
	
	#StampaDizionario(decode)
	
	
	#ordino le singole liste di lettere su una lettera per frequenza,
	#e poi le lettere per frequenza dell'accoppiamento migliore
	lDecode = dic2list(decode)
	for i in lDecode:
		SortFreqences(i[1])
	Sort(lDecode, lambda x, y: x[1][0][1]<y[1][0][1])
	
	#scalo la lista associando sempre la prima possibilità se non è già
	#associata, altrimenti la elimino e riordino la lista
	
	#se ad una lettera non rimane nessuna possibilità, metto un segno
	#di riconoscimento (si potrebbe scrivere un algoritmo per trovare la
	#combinazione di lettere tale che la somma totale delle frequenze sia
	#massima ma non so come)
	
	encode = {}
	while not len(lDecode) == 0:
		k = lDecode.pop(0)
		if len(k[1]) == 0:
			encode[k[0]] = '*'
		elif not k[1][0][0] in encode:
			encode[k[1][0][0]] = k[0]
		else:
			del k[1][0]
			lDecode.append(k)
	StampaDizionario(encode)
	
	decode = invert(encode)
	
	fh = open(P, 'r', encoding="utf-8")
	s = fh.read()
	fh.close()
	code = Encode(s, decode)
	print (code)
	

if __name__ == "__main__":
	fh = open(_data, 'r', encoding="utf-8")
	s = fh.read()
	fh.close()
	s = PulisciTesto(s, '“—«„»,.').lower()
	s = PulisciTestoASCII(s, nospace=False)
	s = s.split(' ')
	text1, text2, text3 = [], [], []
	for t in s:
		if(len(t)) == 1:
			text1.append(t)
		if(len(t)) == 2:
			text2.append(t)
		if(len(t)) == 3:
			text3.append(t)
	t2 = ''
	for t in text2:
		t2 += t
	t2 = CalcolaFrequenza(ContaCaratteri(t2))
	t2 = dic2list(t2)
	SortFreqences(t2)
	print (t2)
