# perm([1,2,3], 2) = ([1], perm([2,3], 1)) + ([2], perm([1,3], 1)) + ([3], perm([1,2], 1))
def perm(arr, k):
    res = []
    if k == 0:
        return [[]]

    for i, el in enumerate(arr):
        rest = arr[:i] + arr[i+1:]

        for p in perm(rest, k-1):
            res.append([el] + p)
    
    return res

print(perm([1,2,3,4], 3))

def perm_count(n, k):
    if k == 0:
        return 1
    if n < k:
        return 0
    
    return n * perm_count(n-1, k-1)
