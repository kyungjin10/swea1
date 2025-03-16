import sys
sys.stdin = open("input.txt", "r")

def in_order(T):
    """ 중위 순회 (In-Order Traversal) """
    if T:
        if left[T] != 0:
            in_order(left[T])
        print(value[T], end='')  # 노드 번호가 아니라, 실제 저장된 문자 출력
        if right[T] != 0:
            in_order(right[T])

Test_case = 10

for tc in range(1, 11):
    N = int(input())
    word = [input().split() for _ in range(N)]

    #print(word)

    left = [0] * (N+1)
    right = [0] * (N+1)
    value = [''] * (N+1)  # 노드 번호에 해당하는 문자 저장

    for data in word:
        node = int(data[0])  # 현재 노드 번호
        #print(data[1])
        print(data)
        value[node] = data[1]  # 해당 노드에 저장된 문자

        if len(data) > 2:  # 왼쪽 자식이 있는 경우
            left[node] = int(data[2])

        if len(data) > 3:  # 오른쪽 자식이 있는 경우
            right[node] = int(data[3])

    print(f"#{tc} ", end="")  # 출력 형식 맞추기
    in_order(1)  # 루트 노드부터 중위 순회 시작
    print()  # 줄 바꿈
