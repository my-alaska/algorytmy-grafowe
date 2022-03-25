from dimacs import *

def Stoer_Wagner(V, L):
    from queue import PriorityQueue
    number_active = V

    class Node:
        def __init__(self):
            self.edges = {}
            self.active = True
            self.deactivatedBy = None
        def addEdge(self, to, weight):
            self.edges[to] = self.edges.get(to, 0) + weight
        def delEdge(self, to):
            del self.edges[to]





    G = [None] + [Node() for i in range(V)]

    for (x, y, c) in L:
        G[x].addEdge(y, c)
        G[y].addEdge(x, c)

    def mergeVertices(G, x, y):
        #dodawanie krawędzi od G do punktów z którymi łączy się y
        for vertex in G[y].edges:
            if vertex != x:
                G[x].addEdge(vertex, G[y].edges[vertex])
                G[vertex].addEdge(x,G[y].edges[vertex])
                G[vertex].edges.pop(y)

        #deaktywacja y
        G[y].active = False
        G[y].deactivatedBy = x

        #zmniejszenie liczby aktywnych wierzchołków
        nonlocal number_active
        number_active -= 1
        return x

    def minumumCutPhase(G):
        a = 1
        while not G[a].active:
            a += 1

        S = {a}
        last = a
        but_last = None
        Q = PriorityQueue()
        weight_to_S = [0]*(V+1)
        for vertex in G[a].edges:
            weight_to_S[vertex] += G[a].edges[vertex]
            Q.put((-1*weight_to_S[vertex], vertex))

        while len(S) != number_active:
            vertex = Q.get()[1]

            if vertex not in S and G[vertex].active:
                S.add(vertex)
                last,but_last = vertex,last

                for v in G[vertex].edges:
                    weight_to_S[v] += G[vertex].edges[v]
                    Q.put((-1*weight_to_S[v], v))

        s,t = last,but_last

        potential_result = 0
        for vertex in G[s].edges:
            potential_result += G[s].edges[vertex]

        mergeVertices(G,s,t)

        return potential_result


    result = float('inf')
    while number_active > 2:
        result = min(result, minumumCutPhase(G))
    return result



V, L = loadWeightedGraph(".\connectivity\\clique200")  # wczytaj graf
print(Stoer_Wagner(V, L))
