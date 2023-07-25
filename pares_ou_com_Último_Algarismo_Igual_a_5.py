x=int(input())
y=int(input())
z=int(input())
cont=0
if(x%2==0):
    cont+=1
elif(x%5==0):
    cont+=1
if(y%2==0):
    cont+=1
elif(y%5==0):
    cont+=1
if(z%2==0):
    cont+=1
elif(z%5==0):
    cont+=1
print(cont)


