def monetine10(tot, x=0, low=0):
	if x > tot:
		return 0
	if x == tot:
		return 1
		
		
	ris = 0
	if low <= 1:
		ris = ris + monetine10(tot, x+1, 1)
	if low <= 2:
		ris = ris + monetine10(tot, x+2, 2)
	if low <= 5:
		ris = ris + monetine10(tot, x+5, 5)
	if low <= 10:
		ris = ris + monetine10(tot, x+10, 10)
	
	return ris
	
def monetine50(tot, x=0, low=0):
	if x > tot:
		return 0
	if x == tot:
		return 1

	ris = 0
	if low <= 1:
		ris = ris + monetine50(tot, x+1, 1)
	if low <= 2:
		ris = ris + monetine50(tot, x+2, 2)
	if low <= 5:
		ris = ris + monetine50(tot, x+5, 5)
	if low <= 10:
		ris = ris + monetine50(tot, x+10, 10)
	if low <= 20:
		ris = ris + monetine50(tot, x+20, 20)
	if low <= 500:
		ris = ris + monetine50(tot, x+50, 50)
	
	return ris

print (monetine10(20))
print (monetine50(100))


