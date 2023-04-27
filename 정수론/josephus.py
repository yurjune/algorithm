from collections import deque

n, k = 7, 3  # 7명중 3번째 사람 계속 제거
dq = deque(i for i in range(1, n+1))
result = []

count = 1
while len(dq)>0:
    item = dq.popleft()
    if count % k != 0:
        dq.append(item)
    else:
        result.append(item)
    count += 1
    
print(result)  # [3, 6, 2, 7, 5, 1, 4]
