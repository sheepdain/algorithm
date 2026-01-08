from collections import deque
import heapq

def solution(priorities, location):
    heap=[]
    queue=deque()
    for i, p in enumerate(priorities):
        queue.append([i,p])
        heapq.heappush(heap,-p)
    cnt=1
    while True:
        high=-heapq.heappop(heap)
        while queue[0][1]!=high:
            sub=queue.popleft()
            queue.append(sub)
        if queue[0][0]==location:
            answer=cnt
            break
        else:
            cnt+=1
            queue.popleft()
    return answer

print(solution([2,1,3,2],2))
print(solution([1,1,9,1,1,1],0))