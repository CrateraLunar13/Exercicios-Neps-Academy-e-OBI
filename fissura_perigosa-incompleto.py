n,f=input().split()
matriz=[]
lista=[]
for i in range(int(n)):
    matriz.append(input())
    lista.append([])
    for c in matriz[-1]:
        lista[-1].append(c)
        
def substituir(a,b,forca):
    if(lista[a][b]=="*"):
        return
    elif(int(lista[a][b])<=int(forca)):
        lista[a][b]="*"
        
if(lista[0][0]<=f):
    lista[0][0]="*"
    for linha in range(int(n)):
        for coluna in range(int(n)):
            
            if(coluna>0 and coluna<int(n)):
                if(lista[linha][coluna-1]=="*"):
                    substituir(linha,coluna,f)
                elif(lista[linha][coluna+1]=="*"):
                    substituir(linha,coluna,f)
                                
            elif(linha>0 and linha<int(n)):
                if(lista[linha-1][coluna]=="*"):
                    substituir(linha,coluna,f)
                elif(lista[linha+1][coluna]=="*"):
                    substituir(linha,coluna,f)
                
    
for i in range(int(n)):
    print(''.join(lista[i]))

