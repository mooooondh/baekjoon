# 2579.py

n= int(input())
m= []
for i in range(n):
    m.append(int(input()))

score= [0]* 301

if(n<= 1):
    print(m[0])
    exit()
if(n<= 2):
    print(m[0]+ m[1])
    exit()

score[0]= m[0]
score[1]= max(m[0]+ m[1], m[1])
score[2]= max(m[0]+ m[2], m[1]+ m[2])

for i in range(3, len(m)):
    score[i]= max(score[i- 2]+ m[i], score[i-3]+ m[i-1]+ m[i])

print(score[n- 1])