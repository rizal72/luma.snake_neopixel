def test(size=16):
    matrix=[[]*size]*size
    for r in range(size):
        for c in range(size):
            matrix[r].append(c)
        print(matrix[r])


test();
