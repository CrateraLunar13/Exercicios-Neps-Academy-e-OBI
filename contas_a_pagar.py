v=int(input())
lista=[]
for i in range(3):
    lista.append(int(input()))
lista.sort()
cont=0
for i in lista:
    if(i<=v):
        cont+=1
        v-=i
print(cont)
    