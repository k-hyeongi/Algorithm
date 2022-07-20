# 정렬된 배열의 정합2
# 정렬된 배열 num1, num2가 주어지고, 각각의 크기는 m, n이다. 
# 정렬을 유지하면서 num1부터 채워나가 num2까지 확장해보자.
# * 추가 설명
# - 병합된 m+n 크기만큼의 공간은 이번엔 존재하지 않는다.
# - num1 배열에 num1, num2 모든 요소를 작은 수부터 채워나가고 num2에 나머지 요소를 정렬 유지해서 넣자.
# - 추가 배열 할당은 없다.

# # test case 1
# num1 = [1,3,5,7]
# m = 4
# num2 = [2,4,8]
# n = 3
# # test case 2 
# num1 = [2,8,10]
# m=3
# num2 = [5]
# n=1
# test case 3
num1 = [2,8,10]
m = 3
num2 = [1,2,5,8,9,12]
n = 6


def mergeSortedList2(num1, m, num2, n) :
    i = m-1
    j = n-1
    while (i >= 0) :  
        while j >= 0 :
            if num1[i] > num2[j] :
                num1[i],num2[j] = num2[j],num1[i]
            else :
                j -= 1  
        i -= 1
        j = n-1        

    num1[:] = sorted(num1)
            

mergeSortedList2(num1, m, num2, n)
print(f"{num1} {num2}")
