m,n=[int(i) for i in input().split()]
lista=[]
ij=[]
cont=0
for i in range(1,m+1):
    lista.append([int(l) for l in input().split()])
p=int(input())
for l in range(p):
    ij.append([int(i) for i in input().split()])
    if(lista[ij[-1][0]-1][ij[-1][1]-1]>0):
        lista[ij[-1][0]-1][ij[-1][1]-1]-=1
        cont+=1
print(cont)