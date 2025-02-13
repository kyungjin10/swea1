import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    arr = input().strip()

    N = len(arr)

    mirror_cnt = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
    mirror_list = []

    for i in arr:
        mirror_list.append(mirror_cnt[i])

    mirror_list.reverse()

    result = ''.join(mirror_list)

    print(f'#{test_case} {result}')