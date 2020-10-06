def courseSchedule2(numCourses, prerequisites):
    def kahns_algo(L, S, graph, incoming_edges):
        while len(S) != 0:
            ele = S.pop()
            L.append(ele)
            t = graph[ele]
            for i in range(len(t)):
                p= t[0]
                t.remove(p)
                incoming_edges[p] = incoming_edges[p] -1
                if incoming_edges[p] == 0:
                    S.add(p)
        if max(incoming_edges) > 0:
            return []
        return L
    incoming_edges = [0]*numCourses
    L = []
    S = set()
    graph = [[] for _ in range(numCourses)]
    for i in prerequisites:
        key, value = i
        graph[value].append(key)
        incoming_edges[i[0]] +=1
    for j in range(len(incoming_edges)):
        if incoming_edges[j] == 0:
            S.add(j)
    kahns_algo(L,S,graph, incoming_edges)
courseSchedule2(2, [[1,0],[0,1]])