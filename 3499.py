import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card_name = input().split()

    first_shuffle = []
    second_shuffle = []
    result_shuffle = []

    if N % 2 == 0:
        K = int(N / 2)
        A = card_name[0:K]
        B = card_name[K:N]
    if N % 2 == 1:
        K = int(N // 2) + 1
        A = card_name[0:K]
        B = card_name[K:N]


    first_shuffle.append(A)
    second_shuffle.append(B)


    if len(first_shuffle[0]) == len(second_shuffle[0]):
        for i in range(K):
            result_shuffle.append(first_shuffle[0][i])
            result_shuffle.append(second_shuffle[0][i])

    if len(first_shuffle[0]) > len(second_shuffle[0]):
        for i in range(K-1):
            result_shuffle.append(first_shuffle[0][i])
            result_shuffle.append(second_shuffle[0][i])
        result_shuffle.append(first_shuffle[0][-1])

    print(f'#{tc}', *result_shuffle)