import sys
sys.stdin = open("input.txt", "r")

import itertools

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a, b, c, d = map(int, input().split())
    nums = list(map(int, input().split()))

    new_list = []
    new_list.extend(a * ['+'])
    new_list.extend(b * ['-'])
    new_list.extend(c * ['*'])
    new_list.extend(d * ['/'])

    cal_list = []

    min_num = float('INF')
    max_num = float('-INF')

    cals = set(itertools.permutations(new_list))    # 중복 방지
    #print(cals)

    for cal in cals:
        #print(cal)
        start_num = nums[0]
        for i in range(N - 1):
            if cal[i] == '+':
                start_num += nums[i+1]
            elif cal[i] == '-':
                start_num -= nums[i+1]
            elif cal[i] == '*':
                start_num *= nums[i+1]
            else:
                start_num = int(start_num / nums[i+1])

        min_num = min(start_num, min_num)
        max_num = max(start_num, max_num)
    #print(f'최솟값: {min_num}, 최댓값: {max_num}')
    print(f'#{tc} {max_num - min_num}')










