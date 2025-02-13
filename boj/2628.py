A, B = map(int, input().split())    #가로, 세로 값
A_list = [0, B]     # 가로방향으로 자르는 값의 리스트 = 세로의 길이
B_list = [0, A]     # 세로방향으로 자르는 값의 리스트 = 가로의 길이
N = int(input())   # 자를 점선 갯수 입력받기 

for tc in range(N):     #자르는 번호 구해서 append 하기
    a, b = map(int, input().split())

    if a == 0:    #가로로 자를 때/ 가로로 자르면 0, 점선번호로 나타내기 때문
        A_list.append(b)
    else:     # = if a == 1:    #세로로 자를 때
        B_list.append(b)

# 추가된 리스트 값 오름차순으로 정렬하기 
A_list.sort()
B_list.sort()

a_max = 0   #가로에서 자르는 번호 중 가장 긴 값 설정
b_max = 0   #세로에서 자르는 번호 중 가장 긴 값 설정

for i in range(1, len(A_list)):   
        #len을 쓴 이유: 리스트에 들어있는 숫자는 자르는 번호인데, 인덱스로 길이를 비교해야 할 
    if a_max < A_list[i] - A_list[i-1]:
        a_max = A_list[i] - A_list[i-1]
    #a_max = max(a_max, A_list[i] - A_list[i-1])
    
for i in range(1, len(B_list)):
        if b_max < B_list[i] - B_list[i-1]:
            b_max = B_list[i] - B_list[i-1]
    #b_max = max(b_max, B_list[i] - B_list[i-1])

result = a_max * b_max
print(result)


    



    