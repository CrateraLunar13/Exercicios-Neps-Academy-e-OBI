n,m=input().split()
n=int(n)
m=int(m)
lista=[]
cont=0
contn=0
for i in range(m):
    lista.append(input().split())
for l in range(m):
    contl=l
    for c in range(n):
        cont+=lista[l].count(str(c))
print(n-cont)
