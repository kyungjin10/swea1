import sys
sys.stdin = open("input.txt", "r")


def generate_permutations(N):
    def permute(arr, chosen, result):
        if len(arr) == 0:  # 모든 숫자를 선택했을 때 결과 리스트에 추가
            result.append([1] + chosen + [1])
            return

        for i in range(len(arr)):
            permute(arr[:i] + arr[i + 1:], chosen + [arr[i]], result)

    numbers = list(range(2, N + 1))  # 2부터 N까지 숫자 리스트 생성
    result = []  # 순열 저장할 리스트
    permute(numbers, [], result)
    return result  # 순열 리스트 반환


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    path = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float('INF')

    possible_path = generate_permutations(N)
    #print(possible_path)


    #경로 인덱스 어쩌고해서 path에서 누적합해주기
    for real_possible_path in possible_path:
        cart_sum = 0
        for k in range(len(real_possible_path)-1):
            cart_sum += path[real_possible_path[k]-1][real_possible_path[k+1]-1]

        min_sum = min(min_sum, cart_sum)

    print(f'#{tc} {min_sum}')
