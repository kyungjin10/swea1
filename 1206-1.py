import sys
sys.stdin = open("input.txt", "r")

T = 10

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    building_view = 0

    for i in range(0,N-4):
        building_high = arr[i:i+5]
        if building_high[2] == max(building_high):
            building_high = building_high[2] - max(building_high[0], building_high[1], building_high[3], building_high[4])
            building_view += building_high

    print(f'#{tc} {building_view}')


