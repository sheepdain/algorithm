
N, M = map(int, input().split())  # NxN 격자, M번의 이동
water_map = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    water_map[i] = list(map(int, input().split()))
commands = []
for i in range(M):
    commands.append(list(map(int, input().split())))

cloud = [[N - 2, 0], [N - 2, 1], [N - 1, 0], [N - 1, 1]]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
for command in commands:
    sub = [[False for _ in range(N)] for _ in range(N)]
    # 구름 이동 후 물의 양 증가
    for i in range(len(cloud)):
        nx = (cloud[i][0] + dx[command[0]] * command[1]) % N
        ny = (cloud[i][1] + dy[command[0]] * command[1]) % N
        cloud[i] = [nx, ny]
        water_map[nx][ny] += 1
        sub[nx][ny] = True
    # 물 복사 버그
    for i in range(len(cloud)):
        cnt = 0
        for j in range(2, 9, 2):
            nx = cloud[i][0] + dx[j]
            ny = cloud[i][1] + dy[j]
            if 0 <= nx < N and 0 <= ny < N and water_map[nx][ny]:
                cnt += 1
        water_map[cloud[i][0]][cloud[i][1]] += cnt
    # 구름 재생성
    cloud = []
    for i in range(N):
        for j in range(N):
            if water_map[i][j] >= 2 and not sub[i][j]:
                cloud.append([i, j])
                water_map[i][j] -= 2

answer = 0
for i in range(N):
    for j in range(N):
        answer += water_map[i][j]

print(answer)