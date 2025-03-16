import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    Tree = [0] * (N+1)

    for _ in range(M):
        i, v = map(int, input().split())
        Tree[i] = v

    for j in range(N, 0, -1):
        if j*2 <= N:
            left = Tree[j*2]
            right = Tree[j*2+1] if (j*2+1) <= N else 0 
            Tree[j] = left + right

    print(f'#{tc} {Tree[L]}')

        

    