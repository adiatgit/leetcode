def justrun(n):
    powerset = []
    def makepermutation(subset):
        if(sum(subset)==n):
            powerset.append(subset)
            return
        for i in range(1, 3):
            if(len(subset) <=n):
                makepermutation(subset + [i+1])
        return

    makepermutation([])
    return len(powerset)
