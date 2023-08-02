n=int(input())
fita=map(int,input().split())
fita=list(fita)

aux=[]
aux1=[]
cont=0


def distancia(a,b,lista):
    if(a<=b):
        lista.append(b-a)
    elif(a>b):
        lista.append(a-b)

    
for i in range(n):
    if(fita[i]==0):
        cont=i
    if(i==0):
        cont=2
    distancia(i,cont,aux)
cont=0 
fita.reverse()
for i in range(n):
    if(fita[i]==0):
        cont=i
    if(i==0):
        cont=1
    distancia(i,cont,aux1)

aux.reverse()

for i in range(n):
    if(aux[i]<= aux1[i]):
        fita[i]=aux[i]
    else:
        fita[i]=aux1[i]
fita.reverse()



string = ' '.join(str(i) for i in fita)
print(string)