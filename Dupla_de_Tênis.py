a=[int(input()) for i in range(4)]
a.sort()
sorteado=(a[3]+a[0]-(a[1]+a[2]))
if(sorteado>0):
    print(sorteado)
else:
    print(-sorteado)



        
