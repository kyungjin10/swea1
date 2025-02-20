T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge_station = list(map(int, input().split()))

    charge_station.append(0)
    charge_station.append(N)
    charge_station.sort()

    charge_cnt = 0
    start = 0

    for i in range(M+2):
        if charge_station[i] - charge_station[i-1] > K:
            charge_cnt = 0
            break
        if charge_station[i] - start > K:
            start = charge_station[i-1]
            charge_cnt += 1

    print(f'#{tc} {charge_cnt}')

