'''
# 시작, 끝 포인터 방식

Q. 배열에서 특정한 합을 가지는 두 원소 찾기
1. 시작, 끝 포인터가 각각 배열의 처음과 끝 인덱스를 가리킨다.
2. 두 요소의 합이 target 보다 작으면 시작 포인터의 인덱스를 증가
3. 두 요소의 합이 target 보다 크면 끝 포인터의 인덱스를 감소
'''

def twoSum(nums, target):
    i = 0
    j = len(nums) - 1
    
    while i < j:
        if nums[i] + nums[j] < target:
            i += 1
        elif nums[i] + nums[j] > target:
            j -= 1
        else:
            break
    return [i, j]