def solution(k, dungeons):
    n=len(dungeons)
    visited=[False]*n
    answer = -1
    
    def dfs(hp, cnt):
        nonlocal answer
        answer=max(answer,cnt)
        
        for i in range(n):
            if not visited[i] and hp>=dungeons[i][0]:
                visited[i]=True
                dfs(hp-dungeons[i][1],cnt+1)
                visited[i]=False

    dfs(k,0)
    
    return answer