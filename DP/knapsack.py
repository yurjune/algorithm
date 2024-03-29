'''
# knapsack 알고리즘
dp[N][K]: N번째 물건까지 살펴 보았을 때, 무게가 K인 배낭의 최대 가치

1) 배낭의 허용 무게보다 현재 물건의 무게가 더 크면 넣지 않는다.
2) 그렇지 않다면 다음 중 더 나은 가치를 선택한다.
2-1) 현재 물건을 넣지 않고 이전 배낭 그대로 가지고 간다.
2-2) 현재 물건의 무게를 뺀 이전 배낭의 최대 가치에 현재 물건의 가치를 더한다.

# 참고: 백준 12865 평범한 배낭

'''

N, K = 4, 7  # N: 물건의 개수, K: 배낭의 최대 수용 무게
W = [0, 6, 4, 3, 5]  # 물건의 무게
V = [0, 13, 8, 6, 12]  # 물건의 가치
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = W[i], V[i]

    for j in range(1, K+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[N][K])  # 14
