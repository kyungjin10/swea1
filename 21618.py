import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    s = input()

    N = len(s)      # 5 10 21
    stack = []


    for i in s:
        if stack and stack[-1] == i:    # stack[-1] 은 맨 마지막으로 추가된 문자를 뜻 함
            stack.pop()
        else:
            stack.append(i)

    print(f'#{test_case} {len(stack)}')




