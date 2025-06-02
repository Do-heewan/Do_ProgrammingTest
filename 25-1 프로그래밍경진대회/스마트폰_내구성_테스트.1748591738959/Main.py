def min_trials(N, K):
    steps = K // 10

    dp = [[0] * (N+1) for _ in range(steps+1)]

    for t in range(1, steps+1):
        for n in range(1, N+1):
            dp[t][n] = dp[t-1][n-1] + dp[t-1][n] + 1
            
            if (dp[t][n] >= steps):
                return t  # 최소 시도 횟수 반환
    return steps  # 최악의 경우 모든 단계 다 확인

N, K = map(int, input().split())

print(min_trials(N, K))