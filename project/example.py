"""PIOTR LUDYNIA
W dalszej części przedstawiłem działanie algorytmu szybszego,
jednak działającego tylko na specyficznych zestawach danych.
mianowicie są takie koszty przejść, że dla danej krawędzi
ich kolejne różnice tworzą ciąg rosnący.
Zmyliły mnie testy ponieważ ten algorytm(my_solve_bad)
przechodził je wszystkie"""


from queue import Queue
from data import runtests

def my_solve(V, k, edges):
    print("Ilosc wierzcholkow: {}, krawedzi: {}".format(V, len(edges)))
    print("Ilosc oddzialow: {}".format(k))

    G = [None] + [{} for i in range(V)]
    for (a, b), distance in edges:
        if b not in G[a].keys():
            G[a][b] = []
        if a not in G[b].keys():
            G[b][a] = []
        for i in range(len(distance) - 1, 0, -1):
            G[a][b].append(distance[i] - distance[i - 1])
        G[a][b].append(distance[0])

    result = 0

    def bfs():
        visited = [False] * (V + 1)
        parents = [None] * (V + 1)
        Q = Queue()
        visited[1] = True
        Q.put(1)
        while not Q.empty():
            a = Q.get()
            for b in G[a].keys():
                if len(G[a][b]) > 0 and not visited[b]:
                    visited[b] = True
                    parents[b] = a
                    if b == V:
                        return parents
                    Q.put(b)
        return parents

    for _ in range(k):
        parents = bfs()
        t = V
        while t != 1:
            p = parents[t]
            dist = G[p][t].pop()
            G[t][p].append(-dist)
            result += dist
            t = p

    def bellman_ford():
        parents = [None] * (V + 1)
        d = [float('inf')] * (V + 1)
        d[1] = 0
        for i in range(V+1):
            for a in range(1, V + 1):
                for b in G[a].keys():
                    if len(G[a][b]) != 0:
                        dist = G[a][b][-1]
                        if d[b] > d[a] + dist:
                            if i == V:
                                return True, parents, b
                            d[b] = d[a] + dist
                            parents[b] = a
        return False, None, None

    while True:
        cycle, parents, t = bellman_ford()
        if cycle == False:
            return result

        for _ in range(V):
            t = parents[t]

        ts = t
        dist = G[parents[t]][t].pop()
        result += dist
        G[t][parents[t]].append(-dist)
        t = parents[t]
        while t != ts:
            dist = G[parents[t]][t].pop()
            result += dist
            G[t][parents[t]].append(-dist)
            t = parents[t]


def my_solve_bad(V, k, edges):

    print("Ilosc wierzcholkow: {}, krawedzi: {}".format(V, len(edges)))
    print("Ilosc oddzialow: {}".format(k))

    G = [ {} for i in range(V+1) ]
    for (a, b), distance in edges:
        G[a][b] = []
        for i in range(len(distance)-1,0,-1):
            G[a][b].append(distance[i] - distance[i - 1])
        G[a][b].append(distance[0])
        G[a][b] = sorted(G[a][b], reverse=True)

    def bellman_ford():
        parents = [None] * (V + 1)
        d = [float('inf')] * (V + 1)
        d[1] = 0
        for _ in range(V):
            for a in range(1, V + 1):
                for b in G[a].keys():
                    if len(G[a][b]) != 0:
                        dist = G[a][b][-1]
                        if d[b] > d[a] + dist:
                            d[b] = d[a] + dist
                            parents[b] = a
        return parents

    result = 0
    for i in range(k):
        parents = bellman_ford()

        t = V
        while t != 1:
            parent = parents[t]
            dist = G[parent][t].pop()

            if parent not in G[t].keys():
                G[t][parent] = []

            G[t][parent].append(-dist)
            result += dist
            t = parent

    return result

runtests(my_solve)
