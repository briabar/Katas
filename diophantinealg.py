def sol_equa(n):
    result = []
    for x in range(1,n//2+3):
        for y in range(1,n//2+3):
            if (x - 2 * y) * (x + 2 * y) == n:
                result.append([x,y])
    return sorted(result, reverse=True)


print(sol_equa(12))#, [[4, 1]])
print(sol_equa(13))#, [[7, 3]])
print(sol_equa(16))#, [[4, 0]])
print(sol_equa(17))#, [[9, 4]])


import math
def sol_equa(n):
    res = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            j = n // i
            if (i + j) % 2 == 0 and (j - i) % 4 == 0:
                x = (i + j) // 2
                y = (j - i) // 4
                res.append([x, y])

    return res
