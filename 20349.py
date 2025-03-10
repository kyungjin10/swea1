import sys
sys.stdin = open("input.txt", "r")

TC = int(input())

for tc in range(1, TC+1):
    N, T = map(int, input().split())       # N=카드의 개수 / T=셔플의 횟수

    card = [0] * N
    # shuffle_card = []
    # first_perfect = []
    # second_perfect = []
    # result_shuffle = []
    overhand_num = int(N // 2.7)     # 올릴 하위 37% 카드 개수
    perfect_num = int(N // 0.5)      # 교차로 섞을 50% 카드 개수

    for num in range(N):
        card[num] = num + 1     # 초기 상태의 카드 생성
    #print(card)

    for i in range(T):
        shuffle_card = []
        first_perfect = []
        second_perfect = []
        result_shuffle = []

        shuffle_card.extend(card[-overhand_num:N])
        shuffle_card.extend(card[0:N-overhand_num])

        if N % 2 == 0:
            K = int(N / 2)
            A = shuffle_card[0:K]
            B = shuffle_card[K:N]
        if N % 2 == 1:
            K = int(N // 2) + 1
            A = shuffle_card[0:K]
            B = shuffle_card[K:N]

        first_perfect.extend(A)
        second_perfect.extend(B)

        if len(first_perfect) == len(second_perfect):
            for j in range(K):
                result_shuffle.append(first_perfect[j])
                result_shuffle.append(second_perfect[j])

        if len(first_perfect) > len(second_perfect):
            for j in range(K-1):
                result_shuffle.append(first_perfect[j])
                result_shuffle.append(second_perfect[j])
            result_shuffle.append(first_perfect[-1])



    print(f'#{tc}', *result_shuffle)


