import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    num, cnt = map(str, input().split())

    # print(num[0])

    def exchange_num(cnt):
        for _ in range(cnt):




