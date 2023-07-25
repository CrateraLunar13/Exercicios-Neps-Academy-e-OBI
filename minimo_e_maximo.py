s=int(input())
a=int(input())
b=int(input())
cont=0
contmaior=0
for i in range(a,b+1):
    for n in str(i):
        cont+=int(n)     
    if(cont==s):
        print(i)
        break
    else:
        cont=0 
for i in range(b,a+1,-1):
    for n in str(i):
        contmaior+=int(n)     
    if(contmaior==s):
        print(i)
        break
    else:
        contmaior=0
     
        