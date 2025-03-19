import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    group_cnt = 0
    apply_paper = {}

    for i in range(0, len(arr), 2):
        key = arr[i]
        value = arr[i + 1]
        if key in apply_paper:
            apply_paper[key].append(value)
        if key not in apply_paper:
            apply_paper[key] = [value]

    print(apply_paper)

    for k in apply_paper.values():
        for j in k:
            if j in apply_paper.keys():
                apply_paper[j].append(apply_paper[])






