import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lines = [list(map(int, input().split())) for _ in range(N)]

    cross_dot = 0

    for i in range(N):
        for j in range(i+1, N):

            if lines[i][0] < lines[j][0] and lines[i][1] > lines[j][1]:
                cross_dot += 1

            if lines[i][0] > lines[j][0] and lines[i][1] < lines[j][1]:
                cross_dot += 1


    print(f'#{tc} {cross_dot}')

