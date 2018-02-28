import Queue as Q
# Given an undirected graph G, find the minimum spanning tree within G.
# A minimum spanning tree connects all vertices in a graph with the smallest
# possible total weight of edges. Your function should take in and return an
# adjacency list structured like this:

def search(G):
    q = Q.PriorityQueue()
    result = {}
    for node in G:
        for edge in G[node]:
            q.put((edge[1], node, edge[0]))
    while not q.empty():
        lightest_edge = q.get()
        if lightest_edge[1] not in result:
            result[lightest_edge[1]] = (lightest_edge[2], lightest_edge[0])
    print result
# A
# |4 \2
# B   C
# |5
# D
search({'A': [('B', 2), ('C', 2), ('E', 7)],
      'B': [('A', 2), ('D', 5)],
      'C': [('A', 2), ('E', 2)],
      'D': [('B', 5), ('F', 10)],
      'E': [('A', 7), ('C', 2)],
      'F': [('D', 10)]})
