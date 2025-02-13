import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_die = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            for a in range(M):
                for b in range(M):
                    s += arr[a+i][b+j]
            if max_die < s:
                max_die = s


    print(f'#{tc} {max_die}')
