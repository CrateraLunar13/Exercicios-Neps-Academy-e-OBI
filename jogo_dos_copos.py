n=int(input())
abc=input()
lista=[]
copos=['A','B','C']
cont=0
for i in range(n):
    lista.append(int(input()))
    if(lista[-1]==1 or lista[-1]==2):
        cont+=1
    elif(lista[-1]==3):
        cont=0
print(copos[copos.index(abc)+cont])
    
