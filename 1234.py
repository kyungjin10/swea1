import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    number = input().split()

    mystery_num = number[1]
    secret_num = []

    for numbers in mystery_num:
        if secret_num and secret_num[-1] == numbers:
            secret_num.pop()
        else:
            secret_num.append(numbers)


    print(f'#{test_case} {"".join(secret_num)}')