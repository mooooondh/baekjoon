# 2839.py

n= int(input())
result= [9999]* (n+ 1)
if(n>= 3):
    result[3]= 1
if(n>= 5):
    result[5]= 1

for i in range(3, len(result)):
    result[i]= min(result[i- 3]+ 1, result[i- 5]+ 1, result[i])

if (result[n]== 9999):
    print(-1)
else:
    print(result[n])