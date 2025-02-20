import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(max(arr))
    buy_cnt = 0
    m = max(arr)
    total_profit = 0

    for i in range(1, N):
        max_idx = i
        arr[i] = m
        if arr[0] == m:
            print(f'#{test_case} 0')
            break
        for j in range(0, i):
            buy_cnt += 1
            total_profit += arr[j] * -1 + m * buy_cnt

    print(f'#{test_case} {total_profit}')

