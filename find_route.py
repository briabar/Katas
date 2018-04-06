from collections import deque
def route(G, N1, N2):
    '''Given a directed graph design an algorithm to find out whether there is a
     route between two nodes.'''
    q = deque(N1)
    seen = set(N1)
    while q:
        current = q.popleft()
        if current == N2:
            return True
        for edge in G[current]:
            if not edge in seen:
                q.append(edge)
                seen.add(edge)
    return False



G = {'A' : ['B', 'C', 'D'],
     'B' : ['C'],
     'C' :[],
     'D': ['E', 'F', 'G'],
     'E' : [],
     'F' : [],
     'G' : []}

print(route(G, 'A', 'G'))
