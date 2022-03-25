"""bfs Ford Fulkerson - Edmonds-Karp"""

from dimacs import *
from queue import *

def bfs(G,v,s,nghbours):
    visited = [False]*v
    parents = [None]*v
    Q = Queue()
    visited[s] = True
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for w in nghbours[u]:
            if (u,w) in G and G[(u,w)] > 0 and not visited[w]:
                visited[w] = True
                parents[w] = u
                Q.put(w)
    return visited, parents

def ford(v,E,s):
    t = v-1
    s -= 1
    G = {}

    nghbours = [ [] for i in range(v)]
    for i in range(len(E)):
        G[(E[i][0]-1,E[i][1]-1)] = E[i][2]
        G[(E[i][1]-1,E[i][0]-1)] = 0
        nghbours[E[i][0]-1].append(E[i][1]-1)
        nghbours[E[i][1] - 1].append(E[i][0] - 1)

    visited, parents = bfs(G, v, s, nghbours)
    f = 0
    while visited[t] is True:
        minoos = float('inf')
        k = t
        while k != s:
            minoos = min(minoos,G[(parents[k],k)])
            k = parents[k]
        k = t
        while k != s:

            G[(k,parents[k])] = G[(k,parents[k])] + minoos
            G[(parents[k],k)] = G[(parents[k],k)] - minoos

            k = parents[k]
        visited, parents = bfs(G, v, s,nghbours)
        f += minoos
    return f


v, E = loadDirectedWeightedGraph( ".\\flow\\grid100x100" )
print(ford(v,E,1))