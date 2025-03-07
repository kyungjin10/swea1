import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = input().strip()

    def decimal_to_binary(n):
        binary_number = ""

        if n == 0:
            return "0"

        # 0보다 클 때까지 2로 나누면서 나머지를 정답에 추가
        while n > 0:
            remainder = n % 2
            binary_number = str(remainder) + binary_number
            n = n // 2

        return binary_number

    result = []

    for i in range(0, len(arr), 7):
        decimal_number = decimal_to_binary(arr[i:i + 7])
        result.append()



    print(f'#{tc}', ' '.join(map(str, decimal_number)))
    #print(f'#{tc}', *decimal_num)