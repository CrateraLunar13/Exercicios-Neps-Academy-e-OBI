n=int(input())
lista=[]
i1=0
i2=0
lista = input().split()
for i in range(n):
    if(lista[i]=='1'):
        if(i1==0):
            i1=1
        else:
            i1=0
    else:
        if(i1==0):
            i1=1
        else:
            i1=0
        if(i2==0):
            i2=1
        else:
            i2=0
print(i1)
print(i2)
    