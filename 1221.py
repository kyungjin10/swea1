import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = input().split()

    alien_dict = {
        'ZRO': 0,
        'ONE': 1,
        'TWO': 2,
        'THR': 3,
        'FOR': 4,
        'FIV': 5,
        'SIX': 6,
        'SVN': 7,
        'EGT': 8,
        'NIN': 9,
    }

    numbers = input().split()       #외계어로 입력받은 숫자
    to_human = []       #숫자를 넣을 빈 리스트

    for alien_number in numbers:        #외계어로 입력받은 숫자를 순회하며
        to_human.append(alien_dict[alien_number])       #새로 만든 빈 리스트에 숫자로 집어 넣기

    to_human.sort()     #리스트에 들어간 숫자를 오름차순으로 정렬
    alien_numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    result = []     #숫자를 넣은 리스트를 다시 외계어로 바꾸기 위한 빈 리스트 생성
    for number in to_human:     #숫자가 들어간 리스트에서 순회하며
        result.append(alien_numbers[number])    #바꾼 결과값을 리스트에 넣기

    print(f'#{tc}')
    print(*result)