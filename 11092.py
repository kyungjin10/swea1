T = int(input().strip())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_num = min(arr)  #arr리스트의 가장 작은 값
    max_num = max(arr)  #arr리스트의 가장 큰 값

    min_idx = arr.index(min_num) + 1  # 최소값의 첫 번째 위치
    max_idx = len(arr) - arr[::-1].index(max_num)  # 최대값의 마지막 위치

    result = abs(max_idx - min_idx)  # 절대값 계산
    print(f'#{tc} {result}')

