import sys
sys.stdin = open("input.txt", "r")

from itertools import combinations

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    high = list(map(int, input().split()))

    min_high = float('INF')

    for nums in range(N+1):
        for comb in combinations(high, nums):
            sum_comb = sum(comb)
            if sum_comb >= B:
                min_high = min(min_high, sum_comb)
                result = min_high - B


    print(f'#{tc} {result}')
