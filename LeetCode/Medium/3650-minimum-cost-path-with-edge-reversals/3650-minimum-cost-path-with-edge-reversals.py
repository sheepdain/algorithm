import heapq

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        road_map = [[] for _ in range(n)]
        for start, end, w in edges:
            road_map[start].append([end, w, True, True])
            road_map[end].append([start, 2 * w, False, False])
        distances = [float('inf')] * n
        distances[0] = 0
        pq = [(0, 0)]
        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            if curr_dist > distances[curr_node]:
                continue
            for i in range(len(road_map[curr_node])):
                next_node, w_node, switch, switch_used=road_map[curr_node][i]
                if switch or (not switch and not switch_used):
                    dist = curr_dist + w_node
                    if dist < distances[next_node]:
                        distances[next_node] = dist
                        road_map[curr_node][i][3] = True
                        heapq.heappush(pq,(dist, next_node))
        if distances[n-1]==float('inf'):
            return -1
        return distances[n-1]