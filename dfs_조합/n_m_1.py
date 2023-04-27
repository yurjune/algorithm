# n개 중 m개 고르기
data = ['a', 'b', 'c', 'd']
n = len(data)
m = 3

visited = [False]*len(data)
result = []

def dfs(node, start, depth):
    if depth == m:
        result.append(node)
        return
    
    for i in range(start, n):
        if visited[i]:
            continue

        item = node + data[i]
        visited[i] = True
        dfs(item, i+1, depth+1)
        visited[i] = False

dfs('', 0, 0)
print(result)