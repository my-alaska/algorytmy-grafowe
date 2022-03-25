"""Dany jest graf nieskierowany G = (V,E), funkcja c: E -> N dająca wagi krawędziom, oraz wyróżnione wierzchołki s i t.
Szukamy scieżki z s do t takiej, że najmniejsza waga krawędzi na tej ścieżce jest jak największa.
Należy zwrócić najmniejszą wagę krawędzi na znalezionej ścieżce.
(W praktyce ścieżki szukamy tylko koncepcyjnie.)"""

from dimacs import *

def longest_shortest(v,E,s,t):

    class find_union_node:
        def __init__(self):
            self.parent = self
            self.rank = 0
    def find(x):
        if x.parent != x:
            x.parent = find(x.parent)  # tutaj przepinamy wierzchołki do samego końca
        return x.parent
    def union(x, y):
        a = find(x)
        b = find(y)
        # stosujemy łączenie według rangi
        if a.rank > b.rank:
            b.parent = a
        else:
            a.parent = b
            if a.rank == b.rank:
                b.rank += 1

    V = [None]*v
    for i in range(v):
        V[i] = find_union_node()

    E = sorted(E, key = lambda w: w[2], reverse = True)

    for i in range(len(E)):
        union(V[ E[i][0] -1 ] , V[ E[i][1] -1 ])
        if find(V[s-1]) == find(V[t-1]):
            print(E[i][2])
            break

v, E = loadWeightedGraph( "./rand1000_100000" )

longest_shortest(v,E,0,1)