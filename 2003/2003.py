# 2003.py

n, m= map(int, input().split())
arr= list(map(int, input().split()))

start= 0
end= 0
check= 0
count= 0

for i in range(n):
    while(check< m and end< len(arr)):
        check+= arr[end]
        end+= 1
    if(check== m):
        count+= 1
    check-= arr[i]

print(count)