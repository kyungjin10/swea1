import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    def arr_sort(arr, N):
        for i in range(N-1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    for i in range(N):
        if i % 2 == 0:

        if i % 2 != 0:
            arr[i]


    # for i in range(N):
    #         if i == 0 or i % 2 == 0:
    #             arr[i] = arr[N-1-i]
    #         if i % 2 != 0:
    #             arr[i] = arr[i-1]

    print(f'#{tc} {arr}')

