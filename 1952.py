import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    charge = list(map(int, input().split()))
    swim_plan = list(map(int, input().split()))

    day_charge = charge[0]
    month_charge = charge[1]
    three_month_charge = charge[2]
    year_charge = charge[3]

    