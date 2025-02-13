import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    str1 = input().strip()
    str2 = input().strip()

    cnt = {}    #str1의 각각 알파벳의 숫자를 셀 빈 딕셔너리 생성

    for i in str1:
        cnt[i] = str2.count(i)      #딕셔너리의 i값은 str2에서의 i값의 갯수

    max_count = max(cnt.values())   #가장 큰 수는 cnt 딕셔너리에 들어있는 values 중 가장 큰 값

    print(f'#{test_case} {max_count}')
