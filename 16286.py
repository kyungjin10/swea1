import sys
sys.stdin = open("input.txt", "r")


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    flower_max = 0      #꽃가루 개수의 최댓값

    for i in range(N):
        for j in range(N):
            s = arr[i][j]       #arr의 현재 위치
            for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:       #방향 설정
                for c in range(1, 2):    #방향 설정 후, 얼만큼 이동할지, 상하좌우 1칸씩이므로 범위(1,2)로 설정
                    ni, nj = i + di*c, j + dj*c     #상하좌우로 이동한 값 설정
                    if 0 <= ni < N and 0 <= nj < N:     #오류 안생기게 범위 설정
                        s += arr[ni][nj]        #상하좌우로 이동하며 각각의 누적합 구하기
                if flower_max < s:      #꽃가루 개수의 최댓값이 누적합보다 작으면
                    flower_max = s      #꽃가루 개수의 최댓값을 누적합으로 재설정

    print(f'#{tc} {flower_max}')