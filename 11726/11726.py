# 11726.py

n= int(input())
tile= [0] * (n+ 1)
tile[1]= 1
if (n>= 2):
    tile[2]= 2

for i in range(3, n+ 1):
    tile[i]= int((tile[i-1]%10007+ tile[i-2]%10007)%10007)

print(tile[n])