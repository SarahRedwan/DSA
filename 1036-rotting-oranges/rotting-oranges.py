class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        time ,fresh=0,0

        rows,cols=len(grid),len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    queue.append([r,c])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        while queue and fresh>0:
            for i in range(len(queue)):
                r,c=queue.popleft()
                for dr,dc in directions:
                    row=r+dr
                    col=c+dc
                    if col<0 or col>=cols or row<0 or row>=rows or grid[row][col]!=1:
                        continue
                    grid[row][col]=2
                    queue.append([row,col])
                    fresh-=1
            time+=1
        if fresh==0:
            return time 
        else:
            return -1

        