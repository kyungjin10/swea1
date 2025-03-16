T = int(input())

def in_order(i):        # 중위 순회 함수
    global num
    if i <= N:
        in_order(i * 2)     # 왼쪽 자식
        Tree[i] = num      # value에 숫자 넣고
        num += 1            # 숫자 1씩 늘려줌
        in_order(i * 2 + 1)     # 오른쪽 자식

for tc in range(1, T + 1):
    N = int(input())
    Tree = [0] * (N + 1)   # 1번부터 N번까지 쓰니까 N+1
    num = 1                 # 1부터 N까지 채울 숫자
    in_order(1)             # 1번이 루트니까 1부터 시작
    print(f"#{tc} {Tree[1]} {Tree[N//2]}")
