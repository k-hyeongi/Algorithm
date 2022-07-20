# 배열에서 다수의 요소 찾기
# 정수형 배열이 주어졌을 때 다수의 요소를 찾아보자.
# 다수의 요소란 배열 내 n/2번(floor(n/2))을 초과하여 나타나는 요소를 나타낸다.
# Ex) 배열 총 요소개수가 9개라면 n/2는 4.5개이고, 즉, 5번 이상 나타나는 요소를 나타내는 것임.
# * 세부 조건
# 배열은 항상 1개 이상의 요소를 가짐. 다수의 수는 무조건 하나 존재한다고 가정.

# # test case 1
# numList = [1]
# test case 2
numList = [8,2,2,2,7,2]

# 해시테이블(딕셔너리)를 이용하여 요소 찾기
# 시간복잡도 - O(n)
def majorityElement(numList) :
    nums = {}
    for i in numList :
        if not nums.get(i) :
            nums[i] = 1
        else :
            nums[i] += 1
        if nums[i] > len(numList)/2 :
            return i    
    return -1

# # 정렬을 이용하여 요소 찾기 (신박함)
# # 시간복잡도 - O(NlogN)
# def majorityElement(numList) :
#     return sorted(numList)[int(len(numList)/2)]
    

print(majorityElement(numList))


