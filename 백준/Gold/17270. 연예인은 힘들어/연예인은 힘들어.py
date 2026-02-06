import sys

input = sys.stdin.readline

V, M = map(int, input().split())  # 약속 장소 후보 수, 약속 장소를 연결하는 총 길의 수

time_map = [[float('inf') for _ in range(V + 1)] for _ in range(V + 1)]
for i in range(V + 1):
    time_map[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    # 1. 중복 간선 중 최솟값 처리 (중요!)
    if c < time_map[a][b]:
        time_map[a][b] = time_map[b][a] = c

J, S = map(int, input().split())  # 지헌이와 성하의 위치

for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            time_map[i][j] = min(time_map[i][j], time_map[i][k] + time_map[k][j])

min_time = float('inf')
res_node = -1
j_time = float('inf')

for node in range(1, V + 1):
    if node == J or node == S: continue
    min_time = min(min_time, time_map[J][node] + time_map[S][node])

for node in range(1, V + 1):
    if node == J or node == S: continue
    curr_j_time = time_map[J][node]
    curr_s_time = time_map[S][node]
    curr_time_sum = curr_s_time + curr_j_time
    if curr_time_sum == min_time:
        if curr_s_time >= curr_j_time:
            if j_time > curr_j_time:
                res_node = node
                j_time = curr_j_time

print(res_node)