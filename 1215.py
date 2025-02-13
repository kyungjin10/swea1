import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())   #찾아야 할 회문의 길이
    arr = [list(map(str, input().split())) for _ in range(8)]    #8*8 크기의 글자판

    mirror_cnt = 0      #회문 갯수 초기화

    for i in range(9-N):
        for j in range(9-N):
            s = arr[i][j]


