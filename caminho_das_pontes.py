n,m=(input().split())
pilares=[i for i in range(int(n))]
stb=[]
qpilares=[]
cont=0
for i in range(int(m)):
    stb.append(input().split())
for c in range(len(stb)):
    for l in stb[c][0]:
        if(l==str(pilares[c])):
            cont+=1
        if(l==str[-1][0]):
            qpilares.append(cont)
print(stb)
print(cont)
print(qpilares)