import heapq

N, M = map(int, input().split())
computer_list = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    computer_list[A].append((B, C))
    computer_list[B].append((A, C))

total_time = [float('inf') for _ in range(N + 1)]
parent = [0] * (N + 1)
total_time[1] = 0
heap = []
heapq.heappush(heap, (0, 1))
while heap:
    curr_time, curr_com = heapq.heappop(heap)
    if total_time[curr_com] < curr_time:
        continue

    for next_com, next_time in computer_list[curr_com]:
        cost = curr_time + next_time
        if cost < total_time[next_com]:
            total_time[next_com] = cost
            parent[next_com] = curr_com  # 부모 노드 갱신
            heapq.heappush(heap, (cost, next_com))
print(N - 1)
for i in range(2, N + 1):
    if parent[i] != 0:
        print(i, parent[i])