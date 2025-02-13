T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_sum = 0
    min_sum = float('INF')

    for i in range(N-M+1):
        s = 0
        for j in range(i, i+M):
            s += arr[j]

        if max_sum < s:
            max_sum = s
        if min_sum > s:
            min_sum = s

    print(f'#{tc} {max_sum - min_sum}')
