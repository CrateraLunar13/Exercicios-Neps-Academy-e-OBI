a,b=[int(i) for i in input().split()]
aentrada=[int(i) for i in input().split()]
bentrada=[int(i) for i in input().split()]
cont=0
resp="N"
for i in aentrada:
    if(i == bentrada[cont]):
        cont+=1
    if(cont==b):
        resp="S"
        break
print(resp)
