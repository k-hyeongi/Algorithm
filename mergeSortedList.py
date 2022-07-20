# 정렬된 배열의 병합
# 정렬된 두 배열(num1, num2)을 정렬을 유지하면서 병합하기
# * 추가 설명
# - num1, num2 각각의 크기는 m과 n개의 요소로 초기화되어 있다.
# - num1은 num1과 num2를 병합하기에 충분한 크기로 할당되어 있다. (m+n개)

# # test case 1
# num1 = [1,2,3]
# m = 3
# num2 = []
# n = 0
# # test case 2
# num1 = [0,0,0]
# m = 0
# num2 = [1,2,3]
# n = 3
# # test case 3
# num1 = [1,2,3,0,0,0]
# m = 3
# num2 = [4,5,6]
# n = 3
# test case 4
num1 = [4,5,6,0,0,0]
m = 3
num2 = [1,2,3]
n = 3

# # 삽입 후 정렬
# # 가장 쉽고 간편한 방법이나 해당 방법이 최선은 아님을 기억해야 한다.
# # 시간복잡도 - O(NlogN)
# def mergeSortedList(num1, m, num2, n) :
#     for (i, v) in enumerate(num2) :
#         num1[m+i] = v
#     num1[:] = sorted(num1)


# 비교 후 삽입
# 시간복잡도 - O(N+M)
def mergeSortedList(num1, m, num2, n) :
    i = m-1
    j = n-1
    k = m+n-1  

    while i >= 0 and j >= 0 :
        if num1[i] < num2[j] :
            num1[k] = num2[j]
            j -= 1
        else :
            num1[k] = num1[i]
            i -= 1
        k -= 1 

    while j >= 0 :
        num1[k] = num2[j]
        k -= 1
        j -= 1 
    

mergeSortedList(num1, m, num2, n)
print(num1)
