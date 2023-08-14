# Q. 주어진 배열에서 구간의 합이 5인 구간의 개수 찾기
# slow, fast runner 방식 이용

data = [1, 2, 3, 2, 5]
N = len(data)
target_sum = 5
partial_sum = data[0]
fast = 0

answer = 0
# slow 를 1씩 증가시키며 반복
for slow in range(N):
    while fast + 1 < N and partial_sum < target_sum:
        fast += 1
        partial_sum += data[fast]
    if partial_sum == target_sum:
        answer += 1
    partial_sum -= data[slow]

print(answer)  # 3 (2-3, 3-2, 5)