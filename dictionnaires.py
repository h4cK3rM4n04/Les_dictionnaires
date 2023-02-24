menagerie = [{'type':'Boa','Nom':'Bob','Age':21},{'type':'Anaconda','Nom':'Alice','Age':18},\
                {'type':'Python','Nom':'Albert','Age':34},{'type':'Vipere','Nom':'Juliette','Age':14},\
                {'type':'Python','Nom':'Max','Age':6}, {'type':'Couleuvre','Nom':'Carry','Age':9},\
                {'type':'Boa','Nom':'Papy','Age':29}]
def age(n,liste):
    final,fi = [],[]
    for i in liste:
        x = list(i.values())
        for j in range(len(x)):
            if x[2]>n:
                final.append(x[1])
    for i in final : 
        if i not in fi: 
            fi.append(i) 
    return fi
print(age(13,menagerie))