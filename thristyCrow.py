def thristyCrow(A, k):
    A.sort()
    no_of_rocks = 0
    for i in range(k):
        no_of_rocks += A[i]*(len(A) -i)
        for j in range(i,k):
            A[j] =A[j] - A[i]
    return no_of_rocks
print(thristyCrow([5,5,10], 1))
