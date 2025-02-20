
keypad = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
    '*': (3, 0), 0: (3, 1), '#': (3, 2)
}

numbers = list(map(int, input().split()))
hand = input().strip()  # "right" 또는 "left"

left_hand = keypad['*']     #왼손의 초기값
right_hand = keypad['#']    #오른손의 초기값

result = ""     #결과 출력할 곳

for i in numbers:      #입력받은 숫자를 순회하는데,
    if i in [1, 4, 7]:  #그 숫자가 1,4,7중에 있으면
        result += "L"   #결과칸에 "l"을 넣겠다
        left_hand = keypad[i]       #왼손은 keypad[i]로 위치 이동

    if i in [3, 6, 9]:  #입력받은 숫자가 3,6,9중에 있으면
        result += "R"   #결과칸에 "R"을 넣겠다
        right_hand = keypad[i]      #오른손 위치 이동

    if i in [2, 5, 8, 0]:   #입력받은 숫자가 2,5,8,0중에 있으면 그 숫자의 위치와 왼손과 오른손의 각 위치의 거리를 계산할 건데,
        left_distance = abs(keypad[i][0] - left_hand[0]) + abs(keypad[i][1] - left_hand[1])
        right_distance = abs(keypad[i][0] - right_hand[0]) + abs(keypad[i][1] - right_hand[1])

        if left_distance < right_distance:    #2,5,8,0중의 숫자와 왼손의 거리가 더 짧으면
            result += "L"       #결과칸에 "L"추가
            left_hand = keypad[i]
        elif left_distance > right_distance:
            result += "R"
            right_hand = keypad[i]
        else:       #만약 오른손과의 거리, 왼손과의 거리가 같으면
            if hand == "left":      #왼손잡이다?
                result += "L"       #"L"추가
                left_hand = keypad[i]
            else:
                result += "R"
                right_hand = keypad[i]

print(result)





