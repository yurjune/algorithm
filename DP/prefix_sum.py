# 누적합(prefix sum)
numbers = [2, 4, 1, -5, 2, -3]
limit = len(numbers)+1

psum = [0]*limit
for i in range(1, limit):
    psum[i] = psum[i-1] + numbers[i-1]
# psum = [0, 2, 6, 7, 2, 4, 1]


'''
- 누적합을 통해 구간합을 구할 수 있다.
- 구간 [i, j] 의 원소들의 합: psum[j+1] - psum[i]
ex) 구간 [2, 5] 가 인덱스 2~5 라고 하면: 1, -5, 2, -3 의 합 = -5
'''

print(psum[6] - psum[2])  # -5