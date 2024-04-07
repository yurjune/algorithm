# 이진탐색

# 1. 반복문 활용
def binary_search(data, target):
    data.sort()
    start, end = 0, len(data)-1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1 
        elif data[mid] < target:
            start = mid + 1
    return -1

# 2. 재귀 활용
def solution(data, target):
    data.sort()
    start, end = 0, len(data)-1

    def binary_search(target, start, end):
        if start > end:
            return -1
        
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1 
        elif data[mid] < target:
            start = mid + 1
    
    return binary_search(target, start, end)