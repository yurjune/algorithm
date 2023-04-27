# 백준 2667 단지번호 붙이기
from collections import deque

# n x m: 세로(열) x 가로(행)
n = int(input())
m = n

graph = [list(map(int, input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(y, x):
    Q = deque()
    Q.append([y, x])
    visited[y][x] = True
    count = 1
    
    while Q:
        y, x = Q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or ny<0 or nx>=m or ny>=n:
                continue
            if visited[ny][nx] or graph[ny][nx] == 0:
                continue

            visited[ny][nx] = True
            Q.append([ny, nx])
            count += 1
            
    return count

result = []
count_all = 0
for y in range(n):
    for x in range(m):
        if not visited[y][x] and graph[y][x] == 1:
            result.append(bfs(y, x))
            count_all += 1

print(count_all)
print(*sorted(result))