def min_trials(N, K):
    # K를 10cm 단위로 나눈 단계 수
    steps = K // 10
    
    # dp[t][n] = t번 시도, n개의 장비로 확인 가능한 최대 단계 수
    dp = [[0] * (N + 1) for _ in range(steps + 2)]  # +2는 범위 초과 방지

    for t in range(1, steps + 2):  # 시도 횟수는 최대 steps까지
        for n in range(1, N + 1):
            # 점화식: dp[t][n] = dp[t-1][n-1] + dp[t-1][n] + 1
            dp[t][n] = dp[t - 1][n - 1] + dp[t - 1][n] + 1
            if dp[t][n] >= steps:
                return t  # 최소 시도 횟수 반환
    return steps  # 최악의 경우 모든 단계 다 확인

N, K = map(int, input().split())

print(min_trials(N, K))