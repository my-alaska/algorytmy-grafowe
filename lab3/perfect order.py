#find perfect elimination order to get chordal graph

from dimacs import *
from lexBFS import *



def check_perfect_order(G, T):
    for i in range(len(T)):
        parent = None
        for j in range(i):
            if T[j] in G[T[i]].out:
                G[T[i]].rn.add(T[j])
                parent = T[j]
        if parent != None and not G[T[i]].rn - {parent} <= G[parent].rn:
            return False
    return True



class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()  # zbiór sąsiadów
        self.rn = set()

    def connect_to(self, v):
        self.out.add(v)

(V, L) = loadWeightedGraph("chordal\interval-rnd50")

G = [None] + [Node(i) for i in range(1, V + 1)]  # żeby móc indeksować numerem wierzchołka

for (u, v, _) in L:
    G[u].connect_to(v)
    G[v].connect_to(u)

print(check_perfect_order(G, lexBFS(G,1)))