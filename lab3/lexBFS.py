from dimacs import *

from queue import *




def lexBFS(G, s):
    V = len(G) - 1

    lista = [set()]
    for i in range(1, V + 1):
        if i != s:
            lista[0].add(i)

    result = [s]
    processed = {s}

    while lista:
        neighbours = G[result[-1]].out

        i = 0
        while i != len(lista):
            Y = lista[i] & neighbours
            K = lista[i] - Y
            l1, l2 = lista[:i], lista[i + 1:]
            if len(K) != 0:
                l1.append(K)
                # i += 1
            if len(Y) != 0:
                l1.append(Y)
                # i += 1
            lista = l1 + l2
            i+=1

        result.append(lista[-1].pop())
        if len(lista[-1]) == 0:
            lista.pop()

    return result


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()  # zbiór sąsiadów

    def connect_to(self, v):
        self.out.add(v)


(V, L) = loadWeightedGraph("chordal\interval-rnd50")

G = [None] + [Node(i) for i in range(1, V + 1)]  # żeby móc indeksować numerem wierzchołka

for (u, v, _) in L:
    G[u].connect_to(v)
    G[v].connect_to(u)


def checkLexBFS(G, vs):
    n = len(G)
    pi = [None] * n
    for i, v in enumerate(vs):
        pi[v] = i

    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            Ni = G[vs[i]].out
            Nj = G[vs[j]].out

            verts = [pi[v] for v in Nj - Ni if pi[v] < i]
            if verts:
                viable = [pi[v] for v in Ni - Nj]
                if not viable or min(verts) <= min(viable):
                    print(vs[i],vs[j])
                    return False
    return True

