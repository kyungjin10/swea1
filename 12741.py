import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    A, B, C, D = map(int, input().split())

    if B <= C or D <= A:
        result = 0
    else:
        a = max(A, C)
        b = min(B, D)
        result = abs(b - a)

    print(f'#{tc} {result}')





