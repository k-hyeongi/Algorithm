# 정렬된 배열에서 중복 제거
# 정렬된 배열의 요소들을 중복 없이 단 1번씩만 가질 수 있게 주어진 배열을
# 있는 그대로 수정하고, 수정된 배열의 새로운 길이를 반환하라 
# * 추가적인 배열 할당 하지 말 것. 중복된 요소를 하나만 남기고 걸러내는 함수를 만드는 것.
# * return된 길이 이후의 데이터는 무시해도 무방하기 때문에 배열의 데이터들에 대해 신경 안 써도 됨.

# test case 1
# nums = [0, 0, 0, 1, 2, 2, 2]
# test case 2
# nums = []
# test case 3
# nums = [1, 2, 3, 4]
# test case 4
nums = [0, 0, 1, 1, 2, 3]

# 선형 순회 방식 (Linear Search) - 시간 복잡도 O(n)
def removeDuplicates(nums) :
    if (len(nums) == 0) :
        return 0

    curr = nums[0]
    leng = 1
    for i in range(1, len(nums)) :
        if (curr != nums[i]) :
            leng += 1
            curr = nums[i]
    
    return leng

print(removeDuplicates(nums))