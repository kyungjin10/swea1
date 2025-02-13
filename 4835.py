
import sys
sys.stdin = open("input.txt", "r")

T = int(input().strip())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_sum = 0
    min_sum = float('INF')

    for i in range(0, N-M+1):
        temp = 0
        for j in range(i, M+i):
            temp = temp + arr[j]

        if max_sum < temp:
            max_sum = temp
        if min_sum > temp:
            min_sum = temp

    print(f'#{test_case} {max_sum - min_sum}')



