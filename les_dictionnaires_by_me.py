menagerie = [{'type':'Boa','Nom':'Bob','Age':21},{'type':'Anaconda','Nom':'Alice','Age':18},\
             {'type':'Python','Nom':'Albert','Age':34},{'type':'Vipere','Nom':'Juliette','Age':14},\
             {'type':'Python','Nom':'Max','Age':6}, {'type':'Couleuvre','Nom':'Carry','Age':9},\
             {'type':'Boa','Nom':'Papy','Age':29}]
f = []
def age(n, liste):
	global f
	for i in liste:
		transf_list = list(i.values())
		if transf_list[2] > n:
			f.append(transf_list[1])
	return f
print(age(13, menagerie))

###Nice===============================================================================================>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>