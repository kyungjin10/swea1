import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    N = arr[0]
    charge = arr[1:]
    charge.append(0)        # 길이 N되게 맞춰줌
    charge_cnt = -1         # 첫번째 정류장에는 횟수 포함 안하니까
    print(charge)

    start = 0   # 스타트 인덱스

    while 0 <= start < N:
        if start + charge[start] >= N - 1:      # 옮긴 스타트 인덱스가 N - 1이상, 즉 목적지에 도착한다면
            charge_cnt += 1                     # 충전 횟수 한 번 더하고 종료
            break

        next_start = start      # 옮겨진 스타트 인덱스 설정 / 계속 옮겨지므로 0이 아닌 start로 설정
        a = next_start
        b = charge[next_start]

        for k in range(1, charge[start]+1):     # 옮길 수 있는 범위
            # 전자는 현재 위치에서 최대로 갈 수 있는 거리
            # 후자는 갈 수 있는 범위(k)값에서 갈 수 있는 거리
            if next_start + charge[next_start] <= start + k + charge[start+k]:      # 후자가 더 값이 크거나 같으면
                next_start = start + k      # 그 인덱스로 바꿔주겠다

        start = next_start      # 그리고 시작지점을 아예 그 많이 갈 수 있는 인덱스 값으로 바꿔줌
        charge_cnt += 1         # 충전 횟수 더해주기

    print(f'#{tc} {charge_cnt}')

