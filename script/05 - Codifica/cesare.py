# coding=utf-8

from codifica import *

_data = 'LeAvventureDiPinocchio.txt'
P = 'testo_segreto_facile.txt'

testo_in_chiaro = """— hai torto, pinocchio! credilo a me, che se non vieni, 
te ne pentirai. dove vuoi trovare un paese più sano per noialtri ragazzi? 
lì non vi sono scuole: lì non vi sono maestri; lì non vi sono libri. 
in quel paese benedetto non si studia mai. il giovedì non si fa scuola: 
e ogni settimana è composta di sei giovedì e di una domenica. 
figurati che le vacanze dell'autunno cominciano col primo di gennaio e 
finiscono coll'ultimo di dicembre. ecco un paese, come piace veramente a 
me! ecco come dovrebbero essere tutti i paesi civili!..."""

def main():
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
	error = 0.25
	
	#Associo ad ogni lettera quelle con la frequenza corrispondente
	#a meno del margine e cerco l'offset più frequente
	offset = {}
	nchar = len(Keys)
	
	for char in f:
		for code in F:
			if F[code] > f[char]*(1-error) and F[code] < f[char]*(1+error):
				#code + off = char (char sono le lettere codificate)
				off = (char2int[char] - char2int[code]) % nchar
				if off in offset:
					offset[off] += 1
				else:
					offset[off] = 1
	
	pOff = dic2list(CalcolaFrequenza(offset))
	SortFreqences(pOff)
	probableOffset = pOff[0][0]
	
	
	
	#Decodifico secondo l'offset trovato
	decode = {}
	
	for char in f:
		#decode[char] = int2char[(char2int[char]-probableOffset)%(nchar)] --> restituiva errore con l'indice 0
		if char2int[char] > probableOffset:
			decode[char] = int2char[(char2int[char]-probableOffset)]
		else:
			decode[char] = int2char[nchar + (char2int[char]-probableOffset)]
	
	fh = open(P, 'r', encoding="utf-8")
	s = fh.read()
	fh.close()
	code = Encode(s, decode)
	print (code)
	

if __name__ == "__main__":
	main()
