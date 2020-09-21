# 2933.py

r, c= map(int, input().split())
cave= []

for i in range(r):
    cave.append(list(map(str, input())))

n= int(input())
height= list(map(int, input().split()))
direction= 0

def dfs(x, y, cave):
    if (x < 0 or y < 0 or x>= c or y>= r or cave[y][x]== "."):
        return

    if (cave[y][x]== "x"):
        cave[y][x] = "o"
        dfs(x + 1, y, cave)
        dfs(x - 1, y, cave)
        dfs(x, y + 1, cave)
        dfs(x, y - 1, cave)
        return

def is_stable(x, y, cave):
    if (x < 0 or y < 0 or x>= c or y>= r or cave[y][x]== "." ):
        return

    if (cave[y][x]!= "."):
        cave[y][x] = "x"
        is_stable(x + 1, y, cave)
        is_stable(x - 1, y, cave)
        is_stable(x, y + 1, cave)
        is_stable(x, y - 1, cave)
        return

def stable_check(cave):
    for i in range(c):
        if(cave[r-1][i]== "x" or cave[r-1][i]== "o"):
            is_stable(i, r-1, cave)

def cluster_fall(cave):
    for i in range(c- 1, -1, -1):
        for j in range(r):
            if(i+ 1< c and cave[i][j]== "o" and cave[i+1][j]== "."):
                cave[i+ 1][j]= "o"
                cave[i][j]= "."

def fall_check(cave):
    for i in range(c):
        for j in range(r):
            if(cave[i][j]== "o"):
                return False
    return True

for i in height:
    stick_loc= r- i

    if(direction== 0):
        for j in range(len(cave[stick_loc])):
            if(cave[stick_loc][j]== "x"):
                cave[stick_loc][j]= "."
                direction= 1
                dfs(j- 1, stick_loc, cave)
                dfs(j+ 1, stick_loc, cave)
                dfs(j, stick_loc- 1, cave)
                stable_check(cave)
                for i in cave:
                    print("".join(i))
                print("======================")
                cluster_fall(cave)
                for i in cave:
                    print("".join(i))
                print("======================")
                stable_check(cave)
                for i in cave:
                    print("".join(i))
                print("======================")
                # while(fall_check(cave)== False):
                #     cluster_fall(cave)
                #     stable_check(cave)
                break
    else:
        for j in range(len(cave[stick_loc])- 1, 0, -1):
            if(cave[stick_loc][j]== "x"):
                cave[stick_loc][j]= "."
                direction = 0
                dfs(j - 1, stick_loc, cave)
                dfs(j + 1, stick_loc, cave)
                dfs(j, stick_loc - 1, cave)
                stable_check(cave)
                cluster_fall(cave)
                stable_check(cave)
                # while (fall_check(cave) == False):
                #     cluster_fall(cave)
                #     stable_check(cave)
                break

for i in cave:
    print("".join(i))
