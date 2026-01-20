from collections import deque

def solution(n, wires):
    answer = n
    adj = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        adj[v1].append(v2)
        adj[v2].append(v1)
        
    def get_count(start, ignore_v1, ignore_v2):
        count = 1
        queue = deque([start])
        visited = [False] * (n + 1)
        visited[start] = True
        
        while queue:
            wire = queue.popleft()
            for near in adj[wire]:
                if (wire == ignore_v1 and near == ignore_v2) or \
                   (wire == ignore_v2 and near == ignore_v1):
                    continue
                
                if not visited[near]:
                    visited[near] = True
                    count += 1
                    queue.append(near)
        return count

    for v1, v2 in wires:
        cnt1 = get_count(v1, v1, v2)
        cnt2 = n - cnt1
        diff = abs(cnt1 - cnt2)
        
        if diff < answer:
            answer = diff
            
    return answer