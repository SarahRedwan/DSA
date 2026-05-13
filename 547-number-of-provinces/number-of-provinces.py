class Solution:
    def findCircleNum(self, isConnected):

        n = len(isConnected)

        self.root=[i for i in range(n)]

        def find(x):
            if self.root[x] != x:
                self.root[x] = find(self.root[x])

            return self.root[x]

        def Union(x, y):

            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                self.root[rootY] = rootX

        for i in range(n):
            for j in range(i + 1, n):

                if isConnected[i][j] == 1:
                    Union(i, j)

        provinces = set()

        for i in range(n):
            provinces.add(find(i))

        return len(provinces)