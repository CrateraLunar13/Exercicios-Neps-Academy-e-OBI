n=int(input())
nomes=[]
valores=[]
for i in range(n):
    nomes.append(input())
    valores.append(int(input()))
x=valores[0]
for i in range(1,n):
    if(x<valores[i]):
        x=valores[i]

print(nomes[valores.index(x)])
print(x)