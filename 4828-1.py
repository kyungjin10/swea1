T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    arr = list(map(int, input().split()))

    max_num = arr[0]
    min_num = arr[0]

    for i in range(N):
        if max_num < arr[i]:
            max_num = arr[i]
        if min_num > arr[i]:
            min_num = arr[i]

    print(f'#{tc} {max_num - min_num}')
