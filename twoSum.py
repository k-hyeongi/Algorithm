# 두 수의 합 찾기
# 주어진 정수형 배열에서 2개의 숫자를 선택하여 더한 값이 특정 target을 만들 때,
# 그 선택한 2개의 정수가 있는 배열의 인덱스를 반환하는 프로그램 작성하기
# 입력값으로 주어지는 배열엔 정확히 하나의 정답이 존재하고 같은 요소의 값을 중복해서 사용할 수 없다.

nums = [2, 3, 8, 9, 11, 12] # 주어지는 정수형 배열
target = 13 # 주어지는 특정 타겟값

# 선형 탐색으로 해결하기 (Linear Search)
def linearSearch(nums, target) :
    for i in range(0, len(nums)) :
        for j in range(i+1, len(nums)) :
            if (nums[i] + nums[j] == target) :
                return [i, j]
    return [-1, -1]
# 주어진 배열을 총 두 번 순회해야 하기 때문에 (이중for문) 시간복잡도는 O(n^2)이 됨.

# HashTable로 해결하기 (Hash Table)
def hashTable(nums, target) :
    hashDict = {}
    for i in range(0, len(nums)) :
        value = target - nums[i]
        if (hashDict.get(value) != None and hashDict[value] != i) :
        # 조건으로 hashDict[value] != i를 추가해주는 이유는 중복되는 경우가 생길 수도 있기 때문.
            return sorted([i, hashDict[value]])
        hashDict[nums[i]] = i
    return [-1, -1]
# 최악의 경우로 주어진 배열을 끝까지 순회해야 할 수도 있기 때문에 시간복잡도는 O(n)이 됨.

result = linearSearch(nums, target)
result = hashTable(nums, target)
print(result)
