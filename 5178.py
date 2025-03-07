import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    arr = ''.join(input().strip() for _ in range(M))

    print(arr)