oggetti = [[175, 10], [90, 9], [20, 4], [50, 2], [10, 1], [200, 20]]

zaino_check = [[0, []]]

def risolvi_check(zaino_check, N, oggetti):
	i = 0
	while i < N:
		max_w = zaino_check[i][0]
		max_id = zaino_check[i][1]
		i += 1
		for _id, ob in enumerate(oggetti):
			k = i - ob[1]
			if k < 0:
				continue
			new_w = zaino_check[k][0] + ob[0]
			if new_w > max_w and not _id in zaino_check[k][1]:
				max_w = new_w
				max_id = zaino_check[k][1] + [_id]
		zaino_check += [[max_w, max_id]]
	return zaino_check

def risolvi_rec(w, oggetti, v=0):
	if oggetti == []:
		return v
	if oggetti[0][1] > w:
		return risolvi_rec(w, oggetti[1:], v)
	
	return max(risolvi_rec(w-oggetti[0][1], oggetti[1:], v+oggetti[0][0]), risolvi_rec(w, oggetti[1:], v))

def risolvi_rec_2(w, oggetti, v=0, solved={}):
	if oggetti == []:
		return v
	if (w, len(oggetti)) in solved:
		return solved[(w, len(oggetti))]
	if oggetti[0][1] > w:
		_max = risolvi_rec_2(w, oggetti[1:], v, solved)
		solved[(w, len(oggetti))] = _max
		return _max
	_max = max(risolvi_rec_2(w-oggetti[0][1], oggetti[1:], v+oggetti[0][0], solved), risolvi_rec_2(w, oggetti[1:], v, solved))
	solved[(w, len(oggetti))] = _max
	return _max
	
print (risolvi_check(zaino_check, 20, oggetti))
print (risolvi_rec(20, oggetti))
print (risolvi_rec_2(20, oggetti))
