def findJudge(N, trust):
    graph = [[None] * N for _ in range(N)]
    for i in trust:
        graph[i[0] - 1][i[1] - 1] = 1
    for j in graph:
        if 1 not in j:
            return graph.index(j) + 1
    return -1
findJudge(3 ,[[1,2],[2,3]])