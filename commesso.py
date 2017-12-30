dist = [
	#       A |
	#		  v
	#Da ->    
	
	[0,2,4,6],
	[2,0,5,7],
	[4,5,0,5],
	[6,7,5,0]

]

N = 4

def risolvi(nodo_partenza, nodi_da_visitare, casi_risolti):
	path = [nodo_partenza] + nodi_da_visitare
	k = len(path)
	
	#ERRORE HASHABLE TYPE
	
	if path in casi_risolti[k].keys():
		
		return casi_risolti[k][path]
	
	
	
	
	if k == 1:
		return -1
	
	
	_min = -1
	for i in nodi_da_visitare:
		ris = risolvi(i, [n for n in nodi_da_visitare if n != i], casi_risolti)
		if ris != -1:
			d = ris + dist[nodo_partenza][i]
			if _min == -1 or d < _min:
				_min = d
	
	casi_risolti[k][path] = _min
	return _min

def main():
	
	casi_risolti = {} #per ogni dimensione c'è un dizionario di casi risolti
	nodo_partenza = 0
	nodi_da_visitare = []
	
	for l,i in enumerate(dist[nodo_partenza]):
		casi_risolti[l+1] = {}
		if l != nodo_partenza:
			casi_risolti[1][l] = i
			nodi_da_visitare += [l]
	
	print (risolvi(nodo_partenza, nodi_da_visitare, casi_risolti))
	
	
	
if __name__ == "__main__":
	main()
