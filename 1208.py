<<<<<<< HEAD
import sys
sys.stdin = open("input.txt", "r")

=======
>>>>>>> 038167e808a5815e806cb56a224594a4f78627a9
T = 10

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):
<<<<<<< HEAD
        arr.sort()      #sort를 for문 안에서 하는 이유: 덤프를 수행할 때마다 최고점과 최저점을 갱신해야 하기 때문임

        if arr[-1] - arr[0] <= 1:   #덤프를 수행하기 전에 평탄화의 여부를 확인해야함
            break

        arr[0] += 1     #덤프 수행
        arr[-1] -= 1

        max_high = max(arr)
        min_high = min(arr)

    print(f'#{tc} {max_high - min_high}')
=======
        arr.sort()
        if arr[-1] - arr[0] <= 1:
            break

        arr[-1] -= 1
        arr[0] += 1

    print(f'#{tc} {max(arr) - min(arr)}')

>>>>>>> 038167e808a5815e806cb56a224594a4f78627a9
