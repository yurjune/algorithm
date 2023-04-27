# 백준 2667 단지번호 붙이기
import sys
sys.setrecursionlimit(100000)

# n x m: 세로(열) x 가로(행)
n = int(input())
m = n

graph = [list(map(int, input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 1
def dfs(y, x):
    global count
    visited[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx<0 or ny<0 or nx>=m or ny>=n:
            continue
        if visited[ny][nx] or graph[ny][nx] == 0:
            continue

        dfs(ny, nx)
        count += 1


result = []
count_all = 0
for y in range(n):
    for x in range(m):
        if not visited[y][x] and graph[y][x] == 1:
            dfs(y, x)
            result.append(count)
            count = 1
            count_all += 1

print(count_all)
print(*sorted(result))