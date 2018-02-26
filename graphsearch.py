# Given an undirected graph G, find the minimum spanning tree within G.
# A minimum spanning tree connects all vertices in a graph with the smallest
# possible total weight of edges. Your function should take in and return an
# adjacency list structured like this:

# {'A': [('B', 2)],
#  'B': [('A', 2), ('C', 5)],
#  'C': [('B', 5)]}


## LOOK INTO Prim's algor.
def prim(G):
    visited = []
    result = []
    for node in G:
        name = node
        adjacency_list = sorted(G[node])
        print name, adjacency_list
        for edge in adjacency_list:
            print edge
            if edge[0] not in visited or edge[0] in visited and edge[1] < result[edge[0]]:
                result.append(edge)
                visited.append(edge[0])
    print result
# A
# |4 \2
# B   C
# |5
# D
prim({'A': [('B', 4), ('C', 2)],
      'B': [('A', 2), ('D', 5)],
      'C': [('A', 4)],
      'D': [('B', 5)]})
