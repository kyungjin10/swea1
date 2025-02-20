import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    N = int(input())   #찾아야 할 회문의 길이
    arr = [list(map(str, input().strip())) for _ in range(8)]    #8*8 크기의 글자판
    #print(arr)

    mirror_cnt = 0      #회문 갯수 초기화

    #가로 탐색
    for i in range(8):
        for j in range(8-N+1):
            s = arr[i][j:j+N]
            #print(s)
            if s == s[::-1]:
                #print(s)
                mirror_cnt += 1
                #print(mirror_cnt)
    #세로 탐색
    for i in range(8-N+1):
        for j in range(8):
            t = arr[i:i+N][j]
            #t = [arr[i+k][j] for k in range(N)]
            #print(s)
            if t == t[::-1]:
                print(t)
                mirror_cnt += 1

    print(f'#{test_case} {mirror_cnt}')
