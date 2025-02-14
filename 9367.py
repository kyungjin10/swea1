import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    carrot_cnt = 1
    max_carrot = 0

    for i in range(N-1):
        if arr[i] < arr[i+1]:
            carrot_cnt += 1

        else:
            carrot_cnt = 1

        max_carrot = max(max_carrot, carrot_cnt)

    print(f'#{tc} {max_carrot}')