# 2933.py

r, c= map(int, input().split())
cave= []

for i in range(r):
    cave.append(list(map(str, input())))

n= int(input())
height= list(map(int, input().split()))
direction= 0

def dfs(x, y):
    global cave
    if (x < 0 or y < 0 or x>= c or y>= r or cave[y][x]== "."):
        return

    if (cave[y][x]== "x"):
        cave[y][x] = "o"
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return

def is_stable(x, y):
    global cave
    if (x < 0 or y < 0 or x>= c or y>= r or cave[y][x]== "." ):
        return

    if (cave[y][x]== "o"):
        cave[y][x] = "x"
        is_stable(x + 1, y)
        is_stable(x - 1, y)
        is_stable(x, y + 1)
        is_stable(x, y - 1)
        return

def stable_check():
    global cave
    for i in range(c):
        if(cave[r-1][i]== "x" or cave[r-1][i]== "o"):
            is_stable(i, r-1)

def cluster_fall():
    global cave
    for i in range(r- 1, -1, -1):
        for j in range(c):
            if(i+ 1< r and cave[i][j]== "o" and cave[i+1][j]== "x"):
                is_stable(j, i)
                return
    for i in range(r- 1, -1, -1):
        for j in range(c):
            if(i+ 1< r and cave[i][j]== "o" and cave[i+1][j]== "."):
                cave[i + 1][j] = "o"
                cave[i][j] = "."

def fall_check():
    global cave
    for i in range(r):
        for j in range(c):
            if(cave[i][j]== "o"):
                return False
    return True

for i in height:
    stick_loc= r- i
    if(direction== 0):
        direction = 1
        for j in range(len(cave[stick_loc])):
            if(cave[stick_loc][j]== "x"):
                cave[stick_loc][j]= "."
                dfs(j- 1, stick_loc)
                dfs(j+ 1, stick_loc)
                dfs(j, stick_loc- 1)
                dfs(j, stick_loc+ 1)
                stable_check()
                while(fall_check()== False):
                    cluster_fall()
                    stable_check()
                break
    else:
        direction = 0
        for j in range(len(cave[stick_loc])- 1, -1, -1):
            if(cave[stick_loc][j]== "x"):
                cave[stick_loc][j]= "."
                dfs(j - 1, stick_loc)
                dfs(j + 1, stick_loc)
                dfs(j, stick_loc - 1)
                dfs(j, stick_loc + 1)
                stable_check()
                while (fall_check() == False):
                    cluster_fall()
                    stable_check()
                break

for i in cave:
    print("".join(i))
