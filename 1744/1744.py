# 1744.py

n= int(input())
m= []
for i in range(n):
    m.append(int(input()))

k= []
l= []
result= 0

m.sort(reverse= True)

for i in m:
    if(i> 1):
        k.append(i)
        if(len(k)== 2):
            result+= k.pop()* k.pop()
    else:
        l.append(i)

if(len(k)!= 0):
    result+= k.pop()

l.sort()

for i in l:
    if(i!= 0 and i!= 1):
        k.append(i)
        if(len(k)== 2):
            result+= k.pop()* k.pop()
    else:
        if(len(k)!= 0 and i== 0):
            result+= k.pop()* i
        elif(len(k)!= 0 and i== 1):
            result+= (k.pop()+ i)
        else:
            result+= i

if(len(k)!= 0):
    result+= k.pop()

print(result)