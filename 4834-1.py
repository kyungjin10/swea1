T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = input().strip()

    cnt = [0] * 10 #0부터 9까지의 카드의 장수를 넣을 공간

    for num in arr:     #arr에서 숫자를 하나씩 뽑아내어
        cnt[int(num)] += 1   #cnt의 각 숫자에 맞는 인덱스에 넣어서 누적합 구하기

    max_num = 0     #가장 많은 카드의 숫자
    max_cnt = 0     #가장 많은 카드의 숫자 장 수

    for i in range(10):     #0~9카드
        if cnt[i] >= max_cnt:
            max_cnt = cnt[i]
            max_num = i

    print(f'#{tc} {max_num} {max_cnt}')


