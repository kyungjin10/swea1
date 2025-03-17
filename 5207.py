import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = [list(map(int, input().split())) for _ in range(2)]

    # A = numbers[0]
    # B = numbers[1]
    # cnt = 0
    #
    # for j in range(M):
    #     if B[j] in A:
    #         cnt += 1
    #
    # print(f'#{tc} {cnt}')
    left_list = []
    right_list = []
    #new_list = []

    #for i in range(N):


    def find_center(l, r):
        new_list = A[l:r]
        center = (l+r)//2
        left_list.append(new_list[l:center])
        right_list.append(new_list[center+1:r+1])

    def find_num(n):
        if n >= center:




