import heapq

game_map = [[0 for _ in range(501)] for _ in range(501)]
move = ((0, -1), (-1, 0), (0, 1), (1, 0))

N = int(input())  # 위험한 구역의 수
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            game_map[x][y] = 1

M = int(input())  # 죽음의 구역
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            game_map[x][y] = -1

game_map[0][0] = 2  # 2라면 이미 방문한 구역
heap = [(0, 0, 0)]
result = -1

while heap:
    curr_life, curr_x, curr_y = heapq.heappop(heap)
    for i in range(4):
        dx, dy = move[i]
        nx = curr_x + dx
        ny = curr_y + dy
        if 0 <= nx <= 500 and 0 <= ny <= 500:
            map_life = game_map[nx][ny]
            if 0 <= map_life <= 1:
                if nx == 500 and ny == 500:
                    result = curr_life + map_life
                    break
                game_map[nx][ny] = 2
                heapq.heappush(heap, (curr_life + map_life, nx, ny))
    if result != -1: # break가 어디서 되는 지 확인하기!!
        break
print(result)