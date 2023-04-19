def getMapping(col=16,rows=16):
    # Create a 16x16 matrix filled with zeros
    matrix = [[0 for x in range(col)] for y in range(rows)]

    # Loop through each row and column of the matrix and fill it with an increasing number
    num = 0
    for i in range(rows):
        if i % 2 == 0:  # Even-numbered rows
            for j in range(col-1, -1, -1):
                matrix[i][j] = num
                num += 1
        else:  # Odd-numbered rows
            for j in range(rows):
                matrix[i][j] = num
                num += 1

    # Flatten the matrix into a single array
    flat_array = [item for sublist in matrix for item in sublist]

    # Print the flattened array
    # print(flat_array)

    return(flat_array)

# getMapping(32,16)
