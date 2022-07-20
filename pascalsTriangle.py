# 파스칼의 삼각형
# 파스칼의 삼각형은 수학의 이항 계수를 삼각형의 형태로 숫자를 배열한 구성이다.
# 파스칼의 삼각형은 처음 두 줄을 제외하고 새로 만들어지는 줄의 새로운 숫자는 윗줄의 왼쪽수 + 오른쪽수로 만들어진다.

# 입력으로 몇 줄을 만들 것인지 받아서 파스칼의 삼각형을 이차원 배열의 형태로 구성하자.

# # test case 1
# numRows = 0
# # test case 2
# numRows = 5
# # test case 3
# numRows = 10

def pascalsTriangle(numRows) :
    pascal = []
    prev = []
    if numRows <= 0 :
        return pascal
    for i in range(numRows) :
        pascal.append([1])
        for j in range(i) :
            if (j != i-1) :
                pascal[i].append(prev[j]+prev[j+1])
            else :
                pascal[i].append(1)
        prev[:] = pascal[i]
    return pascal



numRows = int(input("Enter the number of rows: "))
pascalList = pascalsTriangle(numRows)
for i in pascalList :
    print(i)