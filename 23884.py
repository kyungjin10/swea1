import sys
sys.stdin = open("input.txt", "r")

T = 10

for tc in range(1, 11):
    N = int(input())
    word = [(input().split()) for _ in range(N)]

    left = [0] * (N+1)      # 왼쪽 노드에 들어갈 어쩌고
    right = [0] * (N+1)     # 오른쪽   
    Tree = [''] * (N+1)     # 각 노드에 넣을 값
    result = []             # 스택에 넣은 값들 계산 할 어쩌고
    new_postlist = []       # 후위순회로 찾은 값들 넣을 어쩌고

    def post_order(v):        # 후위순회 함수 어쩌고해서 스택에 넣어 그담에 하나씩 빼서 어쩌고 
        if v:
            if left[v] != 0:
                post_order(left[v])
            if right[v] != 0:
                post_order(right[v])    
            new_postlist.append(Tree[v])


    for data in word:       # 트리에 값 넣는 거
        node = int(data[0]) 
        Tree[node] = data[1]

        if len(data) > 2:  # 왼쪽 자식이 있는 경우
            left[node] = int(data[2])

        if len(data) > 3:  # 오른쪽 자식이 있는 경우
            right[node] = int(data[3])

    post_order(1)

    for token in new_postlist:
        if token not in ['+', '-', '/', '*']:   # 숫자면
            result.append(float(token))        # 그 숫자를 결과(스택)에 넣어
        else:                           # 숫자가 아니며는
            b = result.pop()      # 
            a = result.pop()
            if token == '+':
                result.append(a + b)
            if token == '-':
                result.append(a - b)
            if token == '/':
                result.append(a / b)
            if token == '*':
                result.append(a * b)

    print(f'#{tc}', int(result.pop()))

    










    # print(f'#{tc}' , end='')
    # post_order(1)
    # print()
    # print(new_postlist)

    