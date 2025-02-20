import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    n_weight = list(map(int, input().split()))    # 각 화물 무게
    t_weight = list(map(int, input().split()))    # 트럭 적재 용량

    max_weight = 0      # 중량이 최대인 무게
    cnt_container = 0   # 옮겨진 컨테이너 개수
    n_weight.sort()
    t_weight.sort()
    n_weight.reverse()
    t_weight.reverse()

    print(n_weight)
    print(t_weight)

    j = 0
    s = 0
    for i in range(N):      #n_weight의 인덱스      # t_weight의 인덱스
            # s = (n_weight[i], t_weight[j])
            if n_weight[i] > t_weight[j]:  # 화물이 트럭 적재보다 큰경우
                j += 1
            if n_weight[i] <= t_weight[j]:
                s += n_weight[i]
                j += 1
            if j == M:
                break

    print(s)


