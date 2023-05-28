'''
최장 공통 부분 수열(LCS)

- i-1는 word1의 현재 index, j-1는 word2의 현재 index라고 할 때,
dp[i][j]는 word1의 i-1까지의 부분수열과 word2의 j-1까지의 부분수열의 공통수열의 길이의 최댓값

- 풀이법
1) 가장 최근에 추가된 글자가 서로 같으면 추가되기 이전의 최댓값에 1을 더한다.
2) 그렇지 않으면 word1의 최근 글자가 추가되기 직전값과 word2의 최근 글자가 추가되기 전의 직전값 중
더 큰 값을 선택한다.

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