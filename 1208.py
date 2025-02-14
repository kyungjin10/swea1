T = 10

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))


max_high = arr[0]
min_high = arr[0]
max_cnt = 0
min_cnt = 0

for i in arr:  # 상자 높이의 최댓값, 최솟값 구하기
    if max_high <= i:
        max_high = i
    if min_high >= i:
        min_high = i
    # print(max_high, min_high)

for k in range(N):
    min_high += 1
print(max_high, min_high)

# print(f'#{tc} {max_high - min_high}')