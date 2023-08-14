# 가장 긴 증가하는 부분수열(LIS)의 길이 출력
data = [10, 20, 10, 30, 20, 50]
n = len(data)
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))  # 4
