T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_sum = float('-inf')  #배열의 값이 모두 음수일 수도 있으니 음의 무한대로 설정

    if N > M:       #무조건 N이 M보다 짧거나 같도록 설정
        A, B = B, A
        N, M = M, N

    for i in range(M-N+1):
        mul_sum = 0     #각 구간에서 곱해준 값들의 합을 넣을 곳 설정
        for j in range(N):
            mul_sum += A[j] * B[j+i]    #A가 더 짧게 설정해뒀으니 A는 그대로고 B의 인덱스만 이동해줌
        
        max_sum = max(max_sum, mul_sum)

    print(f'#{tc} {max_sum}')

        