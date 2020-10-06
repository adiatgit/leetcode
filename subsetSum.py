def subset(listOfNodes,sum,i):

    remaining = listOfNodes[i:]
    subset(remaining, sum, i+1)






subset(listOfNodes,5,1)
