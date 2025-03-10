import sys
sys.stdin = open("input.txt", "r")


TC = int(input())

for tc in range(1, TC+1):
    N, T = map(int, input().split())       # N=카드의 개수 / T=셔플의 횟수

    card = [0] * N
    shuffle_card = []
    overhand_num = int(N // 2.7)     # 올릴 하위 37% 카드 개수
    perfect_num = int(N // 0.5)      # 교차로 섞을 50% 카드 개수

    for num in range(N):
        card[num] = num + 1     # 초기 상태의 카드 생성
    #print(card)

def overhand_shuffle():
    card[-overhand_num:N]





    #print(f'#{tc}', *card)


