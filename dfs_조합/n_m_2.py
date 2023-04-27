# n개 중 m개 고르기 + 이전 요소 가능 + 중복 가능
data = ['a', 'b', 'c']
n = len(data)
m = 3

result = []

def dfs(node, depth):
    if depth == m:
        result.append(node)
        return
    
    for i in range(0, n):
        item = node + data[i]
        dfs(item, depth+1)

dfs('', 0)
print(result)