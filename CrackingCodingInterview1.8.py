# Cracking the Coding Interview 1.8
# Write an algorithm such that if an element in an MxN matrix is 0,
# it's entire row and column are set to 0.
# [[1,2,3],
#   1,0,3],
#   1,2,3]]


def zero_matrix(m):
    height = len(m)
    width = len(m[0])
    places_to_change = []
    for row in range(height):
        for column in range(width):
            if m[row][column] == 0:
                places_to_change.append([row, column])
    for place in places_to_change:
        for i in range(len(m[place[0]])):
            m[place[0]][i] = 0
        for i in range(height):
            m[i][place[1]] = 0
    print m


zero_matrix([[1, 2, 3], [1, 0, 3], [1, 2, 3]])
zero_matrix([[0, 2, 3], [1, 0, 3], [1, 2, 0]])
zero_matrix([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 0]])
zero_matrix([[0, 2, 3], [1, 0, 3], [1, 2, 3]])
