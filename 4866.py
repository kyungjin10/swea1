import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    arr = input()

    stack = []
    ans = 1     # 짝이 맞다고 가정

    pair = {')': '(', '}': '{'}


    for x in arr:
        if x in '({':
            stack.append(x)
        #print(stack)
        elif x in ')}':
            print(stack[-1])
            if not stack or stack[-1] != pair[x]:       # stack[-1]은 {{(( / ((( / {{(( = 스택의 가장 위에 있는 요소. 가장 최근에 추가된 여는 괄호
                ans = 0
                break
            stack.pop()

    if stack:   # 스택 안이 비어있지 않으면
        ans = 0

    print(f'#{test_case} {ans}')


