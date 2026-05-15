from typing import List
import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        new_task=[]
        

        for i,(enq,pro) in enumerate(tasks):
            new_task.append((enq,pro,i))
        new_task.sort()

        i=0
        result=[]
        time=0
        n=len(tasks)
        heap=[]


        while i<n or heap:
            if not heap and time<new_task[i][0]:
                time=new_task[i][0]
            while i<n and new_task[i][0]<=time:
                enq,pro,idx=new_task[i]

                heapq.heappush(heap,(pro,idx))
                i+=1
            
            pro,idx=heapq.heappop(heap)
            time+=pro
            result.append(idx)
        return (result)



























        # new_tasks=[]
        # result=[]
        # heap=[]

        # for i ,(enq,pro)in enumerate(tasks):
        #     new_tasks.append((enq,pro,i))
        # new_tasks.sort()

        # i=0
        # time=0
        # n=len(tasks)

        # while i<n or heap:
        #     if not heap and time<new_tasks[i][0]:
        #         time=new_tasks[i][0]

        #     while i<n and new_tasks[i][0]<=time:
        #         enq,pro,ixd=new_tasks[i]

        #         heapq.heappush(heap,(pro,ixd))

        #         i+=1
            
        #     pro,ixd=heapq.heappop(heap)
        #     time+=pro
        #     result.append(ixd)
        # return(result)



       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # new_tasks = []

        # for i, (enq, proc) in enumerate(tasks):
        #     new_tasks.append((enq, proc, i))

        # # sort by enqueue time
        # new_tasks.sort()

        # heap = []
        # result = []

        # time = 0
        # i = 0
        # n = len(tasks)

        # while i < n or heap:

        #     # if cpu is idle, jump to next task time
        #     if not heap and time < new_tasks[i][0]:
        #         time = new_tasks[i][0]

        #     # push all available tasks
        #     while i < n and new_tasks[i][0] <= time:
        #         enq, proc, idx = new_tasks[i]

        #         # heap ordered by processing time then index
        #         heapq.heappush(heap, (proc, idx))

        #         i += 1

        #     # process best task
        #     proc, idx = heapq.heappop(heap)

        #     time += proc
        #     result.append(idx)

        # return result