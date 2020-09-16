# 10162.py

n= int(input())
result= [0, 0, 0]

if(n% 10!= 0):
    print(-1)
else:
    while(n!= 0):
        if(n>= 300):
            result[0]= n// 300
            n= n%300
        elif(n>= 60):
            result[1] = n // 60
            n = n % 60
        elif(n>= 10):
            result[2]= n // 10
            break

    print(result[0], result[1], result[2])
