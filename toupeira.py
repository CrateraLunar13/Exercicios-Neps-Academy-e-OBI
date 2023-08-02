s,t=[int(i) for i in input().split()]
mapa=[[0 for i in range(s)] for l in range(s)]
for i in range(t):
    x,y=[int(i)for i in input().split()]
    mapa[x-1][y-1]=1
    mapa[y-1][x-1]=1
p=int(input())
possiveis=p
for l in range(p):
    passeio=[int(i) for i in input().split()]
    for i in range(1,passeio[0]):
        if(mapa[passeio[i]-1][passeio[i+1]-1]==0):
            possiveis-=1
            break
print(possiveis)


