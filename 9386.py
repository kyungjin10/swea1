T = int(input().strip())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().strip()))

    max_cnt = 0 #연속된 1의 최댓값
    cnt_1 = 0   #연속된 1의 갯수

    for i in arr:
        if i == 1:
            cnt_1 += i
        else:
            cnt_1 = 0

        max_cnt = max(cnt_1, max_cnt)

    print(f'#{tc} {max_cnt}')
