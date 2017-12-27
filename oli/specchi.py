stanza = []

def inizia(R, C):
	global stanza
	for i in range(R):
		a = []
		for t in range(C):
			a.append(0)
		stanza.append(a)

	
if __name__ == "__main__":
	inizia(3,4)
	print (stanza)
	
