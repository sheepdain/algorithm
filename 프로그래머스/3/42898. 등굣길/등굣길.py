def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1

    for x, y in puddles:
        dp[y][x] = -1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i == 1 and j == 1) or dp[i][j] == -1:
                continue
                
            if dp[i][j - 1] != -1:
                left = dp[i][j - 1]
            else:
                left = 0
            if dp[i - 1][j] != -1:
                top = dp[i - 1][j]
            else:
                top=0

            dp[i][j] = (left + top) % 1_000_000_007

    return dp[n][m]