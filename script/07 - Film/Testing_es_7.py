# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:47:43 2017

@author: gualandi
"""

# Parse a file where for each row we have:
#  user id | age | gender | occupation | zip code
#  1|24|M|technician|85711
def ParseUsers(filename):
	fh = open(filename, 'r', encoding="utf-8")
	Rs = []
	for i in fh:
		i = i.replace('\n', '')
		Rs += [i.split('|')]
	return Rs

def Count(Ls, i):
	D = {}
	for t in Ls:
		if t[i] in D:
			D[t[i]] += 1
		else:
			D[t[i]] = 1
	return D

def CountGender(Ls):
	return Count(Ls, 2)

def CountOccupation(Ls):
	return Count(Ls, 3)

def CountAge(Ls):
	R = [0,0,0,0,0]
	for t in Ls:
		x = int(t[1])
		if x < 18:
			R[0] += 1
		elif x < 25:
			R[1] += 1
		elif x < 40:
			R[2] += 1
		elif x < 65:
			R[3] += 1
		else:
			R[4] += 1         
	return R
			
# Info for each film:
#  movie id | movie title | release date | video release date |
#          IMDb URL | unknown | Action | Adventure | Animation |
#          Children's | Comedy | Crime | Documentary | Drama | Fantasy |
#          Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
#          Thriller | War | Western |
def ParseFilm(filename):
	fh = open(filename, 'r', encoding="ISO-8859-1")
	Rs = {}
	
	for i in fh:
		i = i.replace('\n', '').split('|')
		
		Rs[i[0]] = i[1:]
		
	return Rs

def CountItem(Fs, i):
	t = 0
	for j in Fs:
		if Fs[j][i] == '1':
			t += 1        
	return t

def CountYears(Fs):
	D = {}
	for i in Fs:
		x = Fs[i][1].split('-')[-1]
		D[x] = D.get(x, 0) + 1
	return D
	
# user id | item id | rating | timestamp
def ParseRatingsOld(filename):
	fh = open(filename, 'r', encoding="utf-8")
	Rs = []
	for i in fh:
		Rs += [i.replace('\n', '').split('\t')]
	return Rs

def CountField(Ls, v):
	return Count(Ls, v)


def PrintTop(Ds, top=5):
	for key in sorted(Ds, key=Ds.get, reverse=True)[:top]:
		print(key, Ds[key])

def PrintTopFilm(Ds, top, Ts):
	for key in sorted(Ds, key=Ds.get, reverse=True)[:top]:
		print(Ts[key][0],'-->', Ds[key])

# user id | item id | rating | timestamp
def ParseRatings(filename):
	fh = open(filename, 'r', encoding="utf-8")
	Rs = {}
	for i in fh:
		try:
			x = i.replace('\n', '').split('\t')
			Rs[(x[0], x[1])] = x[2]
		except: 
			pass
	return Rs

def ComputeAverage(Ls):
	n = len(Ls)
	m = 0
	for i in Ls:
		m += int(Ls[i])
	return m/n

def ComputeIdAverage(Ls, F):
	avg = {}
	count = {}
	for i in Ls:
		_id = F(i)
		mean = avg.get(_id, 0)
		k = count.get(_id, 0)
		mean = mean * k + int(Ls[i])
		k += 1
		mean = mean / k
		avg[_id] = mean
		count[_id] = k
	return avg

def ComputeItemAverage(Ls):
	return ComputeIdAverage(Ls, lambda x: x[1])

def ComputeUserAverage(Ls):
	return ComputeIdAverage(Ls, lambda x: x[0])

def ComputeUserTypeAverage(Ls, Us):
	#chiave categoria -> media voti della categoria
	return ComputeIdAverage(Ls, lambda x: Us[x[0]][2])

def List2Dic(Ls):
	dic = {}
	for i in Ls:
		dic[i[0]] = i[1:]
	return dic

def PredictAvg(Ls, Avg):
	predict = {}
	for i in Ls:
		predict[i] = round(Avg)
	return predict

def RMSE(Ls, _Ls):
	rmse = 0
	for key in Ls:
		rmse += (int(_Ls[key]) - int(Ls[key])) ** 2
	return (rmse / len(Ls))**0.5

def PredictIdAverage(Ls, Avg, F, global_avg):
	predict = {}
	for i in Ls:
		predict[i] = round(Avg.get(F(i), global_avg)) 
	return predict

def PredictItemAverage(Ls, test, global_avg):
	avg = ComputeIdAverage(Ls, lambda x: x[1])
	return PredictIdAverage(test, avg, lambda x: x[1], global_avg)

def PredictUserAverage(Ls, test, global_avg):
	avg = ComputeIdAverage(Ls, lambda x: x[0])
	return PredictIdAverage(test, avg, lambda x: x[0], global_avg)

def PredictUserTypeAverage(Ls, Us, test, global_avg):
	avg = ComputeIdAverage(Ls, lambda x: Us[x[0]][2])
	return PredictIdAverage(test, avg, lambda x: Us[x[0]][2], global_avg)


def GetDist(v1, v2, films, users):
	# Info for each film:
	#  movie id | movie title | release date | video release date |
	#          IMDb URL | unknown | Action | Adventure | Animation |
	#          Children's | Comedy | Crime | Documentary | Drama | Fantasy |
	#          Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
	#          Thriller | War | Western |
	
	dist = 0
	
	filmId1, userId1 = v1
	filmId2, userId2 = v2
	
	if filmId1 == filmId2:
		dist += 50
	else:
		try:
			film1 = films[filmId1]
			film2 = films[filmId2]
		except KeyError:
			return 0
		
		#40% del peso deriva dalla tipologia di film
		for i in range(5, 23):
			if film1[i] == film2[i] and film1[i] == 1:
				dist += 40
		
		#5% dalla distanza di età
		try:
			age1 = int(film1[1].split('-')[2])
			age2 = int(film2[1].split('-')[2])
			dist += 5 - abs(age1 - age2)/20
		except:
			pass
		
	
	if userId1 == userId2:
		dist += 50
	else:
		try:				
			user1 = users[userId1]
			user2 = users[userId2]
		except KeyError:
			return 0
		#5% dall'occupazione
		if user1[2] == user2[2]:
			dist += 5
		
		#10% del gender
		if user1[1] == user2[1]:
			dist += 10
		
		#30% età
		dist += 30 - abs(int(user1[0])-int(user2[0]))/2
		
		#  user id | age | gender | occupation | zip code
		
	
	return dist/100

def PredictAvgDist():
	Rs = ParseRatings('u5.base')
	Test = ParseRatings('u5.test')
	
	users = List2Dic(ParseUsers('u.user'))
	films = ParseFilm('u.item')
	
	prev = {}
	
	tot = 0
	d = len(Test)/100
	
	
	for t in Test:
		tot += 1
		if (tot*100) % d == 0:
			print ('Stato: ', tot/d, '%')
		count = 0
		avg = 0
		
		for i in Rs:
			dist = GetDist(i, t, films, users)
			count += dist
			avg += dist * int(Rs[i])
		
		try:
			prev[t] = round(avg/count)
		except ZeroDivisionError:
			prev[t] = 3
	
	return prev
		

#-----------------------------------------------
# MAIN function: da usare in fase di test
#-----------------------------------------------
if __name__ == "__main__":
	
	Ls = ParseUsers('u.user')
	
	Os = CountOccupation(Ls)
	
	#Ls = ParseFilm('u.item')
	#Fs = CountYears(Ls)
	
	#print (Ls)
	#print (List2Dic(Ls))
	Rs = ParseRatings('u5.base')
	Test = ParseRatings('u5.test')
	global_avg = ComputeAverage(Rs)
	#print (ComputeItemAverage(Rs))
	#print (ComputeUserAverage(Rs))
	#print (ComputeUserTypeAverage(Rs, List2Dic(Ls)))
	predAvg = PredictAvg(Test, ComputeAverage(Rs))
	predAvg1 = PredictItemAverage(Rs, Test, global_avg)
	predAvg2 = PredictUserAverage(Rs, Test, global_avg)
	predAvg3 = PredictUserTypeAverage(Rs,List2Dic(Ls), Test, global_avg)

	
	print ('Errore media generale: ',RMSE(Test, predAvg))
	print ('Errore media film: ',RMSE(Test, predAvg1))
	print ('Errore media utenti: ',RMSE(Test, predAvg2))
	print ('Errore media tipi utente: ',RMSE(Test, predAvg3))
	print ('Errore media distanza: ',RMSE(Test, PredictAvgDist()))	
	
	
