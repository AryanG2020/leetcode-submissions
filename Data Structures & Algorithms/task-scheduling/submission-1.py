from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasksMap=Counter(tasks)
        taskHeap=[-i for i in tasksMap.values()]
        heapq.heapify(taskHeap)
        
        q=deque() #To store time and frequency
        time=0
        while taskHeap or q: #If either heap or queue exists
            time+=1
           
            if taskHeap:
                if taskHeap[0]<-1:
                    q.append((time+n, heapq.heappop(taskHeap)+1))
                else:
                    heapq.heappop(taskHeap)
            if q and q[0][0]==time: #This if statement always goes second
                heapq.heappush(taskHeap, q.popleft()[1])
        return time
        

            
            

        
                
            

            





 
        