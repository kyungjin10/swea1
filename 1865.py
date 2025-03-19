import sys
sys.stdin = open("input.txt", "r")

from itertools import permutations

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    nums = [i for i in range(N)]
    #print(nums)

    max_mul = 0

    for p in permutations(nums):
        mul_result = 1
        for i in range(N):
            mul_result *= arr[i][p[i]] * 0.01
        #print(mul_result)
        max_mul = max(max_mul, mul_result)

    print(f'#{tc} {round(max_mul * 100 + 1e-8, 6):.6f}')
