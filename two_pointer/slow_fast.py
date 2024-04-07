'''
# slow, fast 포인터 방식

Q. 중복된 원소 제거하기
1. slow 와 fast 가 각각 첫 번째, 두 번째 인덱스를 가리킨다.
2. fast 가 전진하면서 slow 와 값이 달라지면, slow 가 한 칸 전진 후에 그 수를 fast 가 가리키는 값으로 바꿔준다.
3. loop 반복 …
4. fast 가 끝에 도달하면 slow 까지의 배열을 슬라이싱하여 반환
'''

def remove_duplicate(nums):
    slow = 0

    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return nums[:slow+1]