T = int(input())   #3

for tc in range(1, T+1):
    N = int(input())    #5
    arr = input().strip()   #49679

    cnt = [0] * 10

    for num in arr:
        cnt[int(num)] += 1

    max_count = 0   #가장 많은 카드의  숫자
    max_number = 0  #가장 많은 카드의 숫자 장 수

    for i in range(10):
        if cnt[i] >= max_count:
            max_count = cnt[i]
            max_number = i

    print(f'#{tc} {max_number} {max_count}')
