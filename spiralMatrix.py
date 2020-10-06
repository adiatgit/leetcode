def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    rowStart = 0
    rowEnd = len(matrix) -1
    columnStart = 0
    columnEnd = len(matrix[0]) -1
    output = []
    while rowStart <= rowEnd and columnStart  <= columnEnd:
        for i in range(columnStart, columnEnd+1):
            output.append(matrix[rowStart][i])
        rowStart+=1
        for i in range(rowStart, rowEnd+1):
            output.append(matrix[i][columnEnd])
        columnEnd-=1
        if rowStart <= rowEnd:
            for i in range(columnEnd, columnStart-1, -1):
                print("3rd",i)
                output.append(matrix[rowEnd][i])
        rowEnd-=1
        if columnStart  <= columnEnd:
            for i in range(rowEnd, rowStart-1, -1):
                print("4th",i)
                output.append(matrix[i][columnStart])
        columnStart+=1
    return output
spiralOrder([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
)