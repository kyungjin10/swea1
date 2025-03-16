import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    node = list(map(int, input().split()))

    left = [0] * (E+2)   # 노드 번호가 1부터 E+1까지임
    right = [0] * (E+2)
    sub_cnt = 0     # 서브트리에 속한 노드의 개수

    for i in range(0, E*2, 2):  
        p, c = node[i], node[i+1]
        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    def dfs(v):
        global sub_cnt
        if v != 0:
            sub_cnt += 1
            dfs(left[v])
            dfs(right[v])

    dfs(N)
    print(f'#{tc} {sub_cnt}')