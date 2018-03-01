def question4(T, r, n1, n2):
    parent_nodes = []
    while n1 != r:
        n1 = get_parent(T, n1)
        if n1 == "error":
            return n1
        parent_nodes.append(n1)
    if len(parent_nodes) == 0:
        return "error"
    while n2 != r:
        n2 = get_parent(T, n2)
        if n2 == "error":
            return n2
        if n2 in parent_nodes:
            return n2
    return "error"


def get_parent(T, n):
    rows = len(T)
    for i in range(0, rows):
        if T[i][n] == 1:
            return i
    return "error"


print question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
