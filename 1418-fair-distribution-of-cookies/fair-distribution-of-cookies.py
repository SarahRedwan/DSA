class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        child = [0] * k
        self.minarr = float('inf')

        def backtrack(i):
            if i == len(cookies):
                self.minarr = min(self.minarr, max(child))
                return

            for j in range(k):
                if child[j] + cookies[i] >= self.minarr:
                    continue

                if j > 0 and child[j] == child[j-1]:
                    continue

                child[j] += cookies[i]
                backtrack(i+1)
                child[j]-=cookies[i]

        backtrack(0)
        return self.minarr