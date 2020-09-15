# 5585.py

n= int(input())
n= 1000- n
result= 0

while(n!= 0):
    if(n >= 500):
        result += n // 500
        n = n % 500
    elif(n >= 100):
        result += n // 100
        n = n % 100
    elif (n >= 50):
        result += n // 50
        n = n % 50
    elif (n >= 10):
        result += n // 10
        n = n % 10
    elif (n >= 5):
        result += n // 5
        n = n % 5
    else:
        result += n
        break

print(result)