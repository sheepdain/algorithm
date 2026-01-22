from collections import deque
def solution(n, edge):
    arr=[[] for _ in range(n+1)]
    for s,e in edge:
        arr[s].append(e)
        arr[e].append(s)
    nums=[0]*(n+1)
    nums[1]=-1
    q=deque()
    q.append((1,0))
    while q:
        idx, cnt=q.popleft()
        for node in arr[idx]:
            if not nums[node]:
                nums[node]=cnt+1
                q.append((node,cnt+1))
    max_num=max(nums)
    answer = 0
    for i in range(n+1):
        if nums[i]==max_num:
            answer+=1
    
    return answer