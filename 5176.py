T = int(input())

def in_order(tree):


for tc in range(1, T+1):
    N = int(input())

    left = [0] * (N+1)
    right = [0] * (N+1)
    parent = [0] * (N+1)

    for i in range(N-1):
        p, c =









    # def in_order(Tree):
    #     if Tree:  # 0이 아니면 (존재하는 정점이면)
    #         in_order(left[Tree])  # 왼쪽 자식(서브트리)로 이동
    #         print(Tree)  # visit(T) T에서 할일 처리
    #         in_order(right[Tree])  # 오른쪽 자식(서브트리)로 이동