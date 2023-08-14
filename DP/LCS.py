'''
최장 공통 부분 수열(LCS)

1. DP가 필요한 문제인지를 검토
겹치는 부분 문제들이 발생하므로 DP로 풀면 좋다.

2. DP 정의
i-1는 word1의 현재 index, j-1는 word2의 현재 index라고 할 때,
dp[i][j]는 word1의 i-1까지의 부분수열과 word2의 j-1까지의 부분수열의 공통수열의 길이의 최댓값

3. 문제를 부분문제들로 분할
word1이 n번째 글자까지, word2가 m번째 글자까지 있고 각각 n, m번째 글자까지 뽑았다고 한다.

1) 각자의 마지막 글자가 서로 같으면 그 글자까지의 공통수열의 최댓값은
마지막 바로 전까지의 공통수열의 최댓값에 1을 더한 값이다.

2) 그렇지 않으면, word1의 n번째, word2의 m-1번째 글자까지의 공통수열의 최댓값과,
word1의 n-1번째, word2의 m번째 글자까지의 최댓값 중에 더 큰 값이 공통수열의 최댓값이다.

- ref
백준 9251
'''

word1 = 'ACAYKP'
word2 = 'CAPCAK'
w = len(word1)
h = len(word2)
dp = [[0]*(h+1) for _ in range(w+1)]

for i in range(1, w+1):
    for j in range(1, h+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[w][h])  # 4