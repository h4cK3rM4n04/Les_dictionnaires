menagerie = [{'type':'Boa','Nom':'Bob','Age':21},{'type':'Anaconda','Nom':'Alice','Age':18},\
             {'type':'Python','Nom':'Albert','Age':34},{'type':'Vipere','Nom':'Juliette','Age':14},\
             {'type':'Python','Nom':'Max','Age':6}, {'type':'Couleuvre','Nom':'Carry','Age':9},\
             {'type':'Boa','Nom':'Papy','Age':29}]

def menage(espece, liste):
    li = []
    for i in liste:
        x = list(i)
        v = list(i.values())
        print(v)
    return li
print(menage('Python', menagerie))