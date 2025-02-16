T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]

    farm_sum = 0
    center = N // 2  # 중심 좌표

    for i in range(N):
        start = abs(center - i)  # 좌측 시작 인덱스
        end = N - start       # 우측 끝 인덱스
        farm_sum += sum(arr[i][start:end])  # 마름모 형태로 더하기

    print(f'#{tc} {farm_sum}')


    # print(arr)

    # #N % 2 = 1   #N은 홀수라는 뜻
    # d = [[0,1],[0,-1],[1,0],[-1,0]]
    # #max_sum = 0
    # #s = 0
    # if N == 1:
    #     s = arr[0][0]
    # else:
    #     for i in range(1, N):
    #         for j in range(1, N):
    #             s = arr[2*i-1][2*j-1]
    #             for di, dj in d:
    #                 for c in range(1, N//2):
    #                     ni, nj = 2*i-1 + c*di, 2*i-1 + c*dj
    #                     if 0 <= ni < N and 0 <= nj < N:
    #                         s += arr[ni][nj]
    #                     # max_sum = max(s, max_sum)

    #         print(f'#{tc} {s}')



