def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """

    # Brute force
    #         for i in matrix:
    #             for j in i:
    #                 if j == target:
    #                     return True
    #         return False
    def binarySearch(l, u, ele, arr):
        if l <= u:
            m = int(l + (u - l) / 2)
            if arr[m] == ele:
                return True
            if ele < arr[m]:
                return binarySearch(l, m - 1, ele, arr)
            elif ele > arr[m]:
                return binarySearch(m + 1, u, ele, arr)
        return False
    row = len(matrix[0])
    for i in matrix:
        if binarySearch(0, len(matrix[0]), target, i) == True:
            return True
    return False

print(searchMatrix(
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
],
5))