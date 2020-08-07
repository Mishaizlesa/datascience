c=[]
for i in range(int(input())):
    c.append(int(input()))
k=0
for i in range (len(c)-4):
    for j in range(4, len(c)-i):
        if (c[i]*c[i+j])%3==0 and (c[i]+c[i+j])%3!=0:
            k+=1
print(k)
print("go")