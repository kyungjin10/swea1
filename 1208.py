T = 10

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
        arr.sort()
        if arr[-1] - arr[0] <= 1:
            break

        arr[-1] -= 1
        arr[0] += 1

    print(f'#{tc} {max(arr) - min(arr)}')

