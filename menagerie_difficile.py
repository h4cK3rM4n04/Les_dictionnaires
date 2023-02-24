menagerie = [{'type':'Boa','Nom':'Bob','Age':21},{'type':'Anaconda','Nom':'Alice','Age':18},\
             {'type':'Python','Nom':'Albert','Age':34},{'type':'Vipere','Nom':'Juliette','Age':14},\
             {'type':'Python','Nom':'Max','Age':6}, {'type':'Couleuvre','Nom':'Carry','Age':9},\
             {'type':'Boa','Nom':'Papy','Age':29}]
def menage(espece,liste) :
    liste.remove(next(x for x in liste[::-1] if x['type'] == espece))
    return liste
print(menage('Boa', menagerie))


#menagerie = [{'type':'Boa','Nom':'Bob','Age':21},{'type':'Anaconda','Nom':'Alice','Age':18},\
             #{'type':'Python','Nom':'Albert','Age':34},{'type':'Vipere','Nom':'Juliette','Age':14},\
             #{'type':'Python','Nom':'Max','Age':6}, {'type':'Couleuvre','Nom':'Carry','Age':9},\
             #{'type':'Boa','Nom':'Papy','Age':29}]

#li = {}

#def menage(espece, liste):
    #for i in liste:
        #for j in range(len(liste)):
            #print (j, i)
    #return liste
#print(menage('Couleuvre', menagerie))
