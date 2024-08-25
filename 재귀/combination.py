# comb([1,2,3], 2) = ([1], comb([2,3], 1)) + ([2], comb([3], 1))
def comb(arr, k):
    res = []
    if k == 0:
        return [[]]

    for i, el in enumerate(arr):
        rest = arr[i+1:]

        for c in comb(rest, k-1):
            res.append([el] + c)
    
    return res
    
print(comb([1,2,3,4], 3))

def comb_count(n, k):
    if k == 0:
        return 1
    if n < k:
        return 0

    return comb_count(n-1, k) + comb_count(n-1, k-1)
