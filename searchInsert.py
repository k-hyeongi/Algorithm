# 배열에서 삽입 위치 찾기
# 정렬된 배열 및 target 목표값이 주어진다.
# 1) 목표값을 찾는다면 배열의 해당 인덱스를 반환한다. 
# 2) 목표값을 찾지 못하면 정렬된 배열이 되도록 목표값이 배열에 들어가야 되는 인덱스값을 구한다.
# * 이 문제는 실제로 배열에 해당 값을 넣어 정렬된 상태로 만드는 것이 아닌, 
# * target값이 있는 위치나 들어가야 하는 위치를 반환하는 문제이다.

# Test Case 1
# nums = [1,2,3,4,5]
# target = 3
# Test Case 2
# nums = [1,4,5,6]
# target = 3
# Test Case 3
# nums = [1,3,5,6]
# target = 0
# Test Case 4
nums = [1,3,5,6]
target = 100

# 순차 탐색 방법 - 시간 복잡도는 최악의 경우에 O(N)
def linearSearchInsert(nums, target) :
    for i in range(0, len(nums)) :
        if (target == nums[i]) :
            return i
        if (target < nums[i]) :
            return i
    return len(nums)

print(linearSearchInsert(nums, target))

# 이진 탐색 방법(Binary Search) - 시간 복잡도는 최악의 경우에 O(logN)
# 만약 데이터가 너무 많아서 시간 복잡도 O(N)보다 빠르게 처리해야 할 조건이 더 붙을 수 있는 경우에 이진 탐색 방법을 떠올려야 한다.

def binarySearchInsert(nums, target) :
    low = 0
    high = len(nums) - 1

    while (low <= high) :
        mid = int((low + high) / 2) # float형이 될 수 있음.
        if (target == nums[mid]) :
            return mid
        if (target > nums[mid]) :
            low = mid + 1
        else :
            high = mid - 1
    
    return low

print(binarySearchInsert(nums, target))
