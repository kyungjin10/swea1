T = int(input())

for tc in range(1, T+1):
    K, N, M = map(int, input().split())     #3 10 5 / 충전 횟수, 총 정류장 수, 충전기 있는 정류장 수
    charge_station = list(map(int, input().split()))   # 1 3 5 7 9 / 충전기가 있는 정류장

    #충전기가 있는 정류장 리스트에 0번과 N번 추가하기.
    #N을 추가하는 이유는 충전기가 있는 정류장의 리스트 인덱스를 비교하여 구할 거기 때문에 마지막 정류장인 N도 추가하여 비교해야됨
    #0을 추가하는 이유는 출발지인 0번째엔 무조건 충전을 하고 가기 때문임
    charge_station.append(0)
    charge_station.append(N)
    charge_station.sort()

    min_charge = 0     # 최소 충전 횟수 
    start = 0       # 새롭게 충전을 하는 지점을 start로 지정

    for i in range(1, M+2):     # M+2인 이유는 0과 N을 리스트에 충전했기 때문임
        if charge_station[i] - charge_station[i-1] > K:     
            #만약 충전기가 있는 정류장이 직전 충전기 정류장과 K 초과만큼 차이가 나면 충전기 설치가 잘못된 거임 -> 종점 도착 X
            min_charge = 0       # 최소 충전 횟수는 0 => 도착을 못함 
            break   

        # 위 경우를 충족하지 않았으니 이 아래의 경우는 충전기가 잘 되어있는 거임!!!!
        if charge_station[i] - start > K:   #만약 충전기 정류장에서 스타트 지점까지 K 초과만큼 차이가 난다면
            start = charge_station[i-1]     #스타트 지점을 직전 충전기 정류장으로 바꿔줄거임
            min_charge += 1     #그러고 최소 충전 횟수를 하나씩 늘림

    print(f'#{tc} {min_charge}')

    # bus_station = [0] * (N+1)       # 총 정류장에 충전기가 있는 정류장은 1로 표시할거임
    # min_charge = N // K      #최소 충전 횟수
    # cnt_0 = 0
    # #print(bus_station)

    # for i in charge_station:
    #     bus_station[i] += 1
    # print(bus_station)

    # for j in bus_station:
    #     if j == 0:
    #         cnt_0 += 1
    #     else:
    #         cnt_0 = 0
    #     max_cnt = max(cnt_0)
    #     print(cnt_0)

    # if cnt_0 == K:
    #     print(f'#{tc} 0')
    # else:
    #     print(f'#{tc} {min_charge}')

    #for j in range(N-K+1):
    #     bus_cnt = bus_station[j:j+K]
    #     print(bus_cnt)
    #     if bus_cnt[j:j+K] == [0] * K :
    #         print(tc)
    #     print(f'#{tc} 0')
    # else:
    #     print(f'#{tc} {min_charge}')

