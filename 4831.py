import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())     #3 10 5 / 충전 횟수, 총 정류장 수, 충전기 있는 정류장 수
    charge_station = list(map(int, input().split()))    # 1 3 5 7 9 / 충전기가 있는 정류장

    bus_station = [0] * (N+1)       # 총 정류장에 충전기가 있는 정류장은 1로 표시할거임
    min_charge = N // K      #최소 충전 횟수
    cnt_0 = 0
    #print(bus_station)

    for i in charge_station:
        bus_station[i] += 1
    print(bus_station)

    for j in bus_station:
        if j == 0:
            cnt_0 += 1
        else:
            cnt_0 = 0
        max_cnt = max(cnt_0)
        print(cnt_0)

    if cnt_0 == K:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {min_charge}')

    #for j in range(N-K+1):
    #     bus_cnt = bus_station[j:j+K]
    #     print(bus_cnt)
    #     if bus_cnt[j:j+K] == [0] * K :
    #         print(tc)
    #     print(f'#{tc} 0')
    # else:
    #     print(f'#{tc} {min_charge}')


