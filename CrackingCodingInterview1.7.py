def rotate_image(matrix):
    height = len(matrix)
    width = len(matrix[0])
    for ix in range(0, height - 1):
        for nx in range(0, height):
            if ix -1 < 0:
                print ix, ix, nx, nx
            else:
                print ix -1, ix
    # 00 10
    # 00 11
    # 00 01
    #
    #00 01
    #00 11
    #00 10
    #
    # 00 02
    # 00 22
    # 00 20
    # 01 12
    # 01 21
    # 01 10



image = [["a","a","a"],
         ["b","b","b"],
         ["c","c","c"]]

rotate_image(image)
