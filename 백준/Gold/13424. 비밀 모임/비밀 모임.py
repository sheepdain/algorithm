T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = [[float('inf') for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        arr[i][i] = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        arr[a][b] = c
        arr[b][a] = c
    K = int(input())
    K_list = list(map(int, input().split()))
    for h in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                arr[i][j] = min(arr[i][j], arr[i][h] + arr[h][j])

    dist = float('inf')
    res_node = 0
    for node in range(1, N + 1):
        dist_sum = 0
        for friend in K_list:
            dist_sum += arr[friend][node]
        if dist_sum < dist:
            dist = dist_sum
            res_node = node
    print(res_node)
