import sys
sys.stdin = open("input.txt", "r")

def pre_order(T):
    if T:
        print(T, end=' ')
        if left[T] != 0:
            pre_order(left[T])
        if right[T] != 0:
            pre_order(right[T])


N = int(input())
E = N - 1
arr = list(map(int, input().split()))

left = [0] * (N+1)
right = [0] * (N+1)

for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c

#print(left)
#print(right)

pre_order(1)    # 1번 부터 전위순회