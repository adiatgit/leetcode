class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        def getEdges(s):
            edges = []
            for i in range(len(self.graph[s])):
                if self.graph[s][i] == 1:
                    edges.append(i)
            return edges

        def dfs(s):
            self.explored.append(s)
            edges = getEdges(s)
            for v in edges:
                if v not in self.explored:
                    dfs(v)
            self.current_label -= 1

        # converting given graph format into adjacency matrix: its important!
        self.graph = [[0 for i in range(numCourses)] for j in range(numCourses)]
        for i in prerequisites:
            self.graph[i[0]][i[1]] = 1

        self.current_label = numCourses
        self.explored = []
        for v in range(numCourses):
            if v not in self.explored:
                dfs(v)

        if self.current_label == 0:
            return True
        return False
s = Solution()
s.canFinish(2, [[0,1],[1,0]])