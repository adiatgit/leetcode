def travellingSalesman(graph):
    dp = [[0 for i in range(len(graph[0]))] for i in range(len(graph))]
    for i in reversed(len(graph[0])):
        for j in reversed(len(graph)):
