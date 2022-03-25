from dimacs import *
from lexBFS import *



def max_clique(G, T):
    V = len(G) - 1

    max = 0
    for i in range(len(T)):
        a = T[i]
        for j in range(i):
            b = T[j]
            if b in G[a].out:
                G[a].rn.add(b)
        if len(G[a].rn) +1 > max:
            max = len(G[a].rn)+1

    return max





class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()
        self.rn = set()


    def connect_to(self, v):
        self.out.add(v)

(V, L) = loadWeightedGraph("maxclique\clique200")

G = [None] + [Node(i) for i in range(1, V + 1)]

for (u, v, _) in L:
    G[u].connect_to(v)
    G[v].connect_to(u)

print(max_clique(G, lexBFS(G,1)))