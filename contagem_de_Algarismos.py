n=int(input())
list=[]
listaux=[[] for i in range(n)]

for i in range(n):
    list.append((input()))
for l in range(n):
    for c in range(10):
        if(str(c) in list[l]):
            listaux[l].append(1)
        else:
            listaux[l].append(0)
print(listaux)

    
        

        
    