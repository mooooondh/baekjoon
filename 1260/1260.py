# 1260.py

from collections import deque

n, m, v= map(int, input().split())
graph= []
for i in range(m):
    graph.append(list(map(int, input().split())))
    pass

visited_1 = [False]* (n+ 1)
visited_1[0]= True
visited_2 = [False]* (n+ 1)
visited_2[0]= True

graph_map= [[] for _ in range(n+ 1)]

for i in graph:
    graph_map[i[0]].append(i[1])
    graph_map[i[1]].append(i[0])
    pass

for i in graph_map:
    i.sort()
    pass

def dfs(graph_in, start, visit):
    visit[start]=True

    print(start, end= " ")

    for i in graph_in[start]:
        if (visit[i]!= True):
            dfs(graph_in, i, visit)
            pass    # end of if
        pass    # end if for
    pass    #end of def

def bfs(graph_in, start, visit):
    queue= deque([start])
    visit[start]= True

    while queue:
        pop_val= queue.popleft()
        print(pop_val, end= " ")
        for i in graph_in[pop_val]:
            if (visit[i]!= True):
                queue.append(i)
                visit[i]= True
                pass    # end of if
            pass    #end of for
        pass    # end of while
    pass    #end of def



dfs(graph_map, v, visited_1)
print()
bfs(graph_map, v, visited_2)