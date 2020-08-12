import re
k={}
with open('URLs.txt', 'r') as f:
    for line in f:
        line=line.strip()[1:]
        if line=="" or line.count("/")==0:
            continue
        else:
            k.setdefault(line[:line.find("/")],0)
            if line[line.find("/")+1:]!="":
                k[line[:line.find("/")]]+=1
print(k)
