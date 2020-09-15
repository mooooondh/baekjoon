# 1463.py

n= int(input())
result= [0]* (n+ 1)
if(n>= 2):
    result[2]= 1
if(n>= 3):
    result[3]= 1

for i in range(4, n+ 1):
    if(i%3== 0 and i% 2== 0):
        result[i] = min(result[i // 3] + 1, result[i // 2] + 1, result[i - 1] + 1)
    elif(i%3== 0):
        result[i] = min(result[i // 3] + 1, result[i - 1] + 1)
    elif(i%2== 0):
        result[i] = min(result[i // 2] + 1, result[i - 1] + 1)
    else:
        result[i] = result[i - 1] + 1

print(result[n])
