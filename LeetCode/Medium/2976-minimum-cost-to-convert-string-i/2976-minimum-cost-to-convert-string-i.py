class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # 알파벳 행렬
        dist = [[float('inf')] * 26 for _ in range(26)]
        for i in range(26):
            dist[i][i] = 0
        
        # 변환 비용
        for u, v, w in zip(original, changed, cost):
            u_idx = ord(u) - ord('a')
            v_idx = ord(v) - ord('a')
            dist[u_idx][v_idx] = min(dist[u_idx][v_idx], w)
            
        # 모든 쌍 최단 경로
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        
        # 변환하는 비용
        total_cost = 0
        n = len(source)
        for i in range(n):
            s_char = source[i]
            t_char = target[i]
            
            if s_char == t_char:
                continue
            
            res = dist[ord(s_char) - ord('a')][ord(t_char) - ord('a')]
            if res == float('inf'):
                return -1
            total_cost += res
            
        return total_cost