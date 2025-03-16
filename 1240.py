import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    all_num = [list(map(int, input().strip())) for _ in range(N)]

    secret_num = []     # 8*56 비번 찾은 리스트
    for i in range(N):
        for j in range(M):
            s = all_num[i][j]
            if s == 1:
                if 0 <= i-1 < N and 0 <= j-1 < M:
                    if all_num[i][j-1] == 0 and all_num[i-1][j] == 0:
                        s = all_num[i][j]
                        secret_num.append(all_num[i:i+8][j:j+56])
                        break
    print(f'#{tc} {secret_num}')

    
                        

