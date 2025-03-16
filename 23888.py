import sys
sys.stdin = open("input.txt", "r")

# def binary_to_decimal(binary_str):
#     decimal_number = 0
#     pow = 0

#     # 뒤에서부터 각 자리의 숫자를 10진수로 변환
#     for digit in reversed(binary_str):
#         if digit == '1':
#             decimal_number += 2 ** pow
#         pow += 1

#     return decimal_number

# result = []
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = "".join(input().strip() for _ in range(N))
    #print(type(arr))

    result = []
    for i in range(0, len(arr),7):
        decimal_num = arr[i:i+7]

        result.append(int(decimal_num, 2))
            

        #print(type(result))
    print(f'#{tc}', *result)