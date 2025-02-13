T = int(input())  #총 테스트케이스 개수

for tc in range(1, T+1):  #첫번째~T까지의 범위 , 케이스별로 처리
    N = int(input())   #케이스 각각의 총 개수
    arr = list(map(int, input().split()))

    max_c = arr[0]  #첫 원소를 최댓값으로 가정
    min_c = arr[0]  #첫 원소를 최솟값으로 가정

    for i in range(1, N):
        if max_c < arr[i]:   #최댓값으로 가정한 값이 arr의 i번째 숫자보다 작으면
            max_c = arr[i]   #최댓값을 arr의 i번째 숫자로 바꿈
        if min_c > arr[i]:
            min_c = arr[i]

    print(f'#{tc} {max_c - min_c}')

'''
3
5
477162 658880 751280 927930 297191
5
565469 851600 460874 148692 111090
10
784386 279993 982220 996285 614710 992232 195265 359810 919192 158175
'''