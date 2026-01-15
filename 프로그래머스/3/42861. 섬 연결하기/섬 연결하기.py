def solution(n, costs):
    # 부모 배열 초기화
    parent = [i for i in range(n)]
    
    # find: 부모(대표) 찾기
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # 경로 압축
        return parent[x]
    
    # union: 두 집합 합치기
    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a
    
    # 비용 기준으로 간선 정렬
    costs.sort(key=lambda x: x[2])
    
    total_cost = 0
    edges_used = 0
    
    # 간선 하나씩 선택
    for a, b, cost in costs:
        if find(a) != find(b):   # 사이클이 아니면 연결
            union(a, b)
            total_cost += cost
            edges_used += 1
            
            if edges_used == n - 1:
                break
    
    return total_cost
