import sys
sys.stdin = open("input.txt", "r")

import itertools

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    charge = [list(map(int, input().split())) for _ in range(N)]

