a, b = map(int, input().split())

days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = ['FRI','SAT','SUN','MON','TUE','WED', 'THU']

sum_days = sum(days[0:a-1]) + b-1

print(day[sum_days % 7])




#5 24

#
# # print(day[0]
# # result = range(1, days[1])
# # print(result)
#
# calender = [list(range(1, num + 1)) for num in days]
#
# for i in range(1, 13):
#     i = days[i]
#     # print(i)
#     for j in range(1, i+1):
#         if j % 7 == 1:
#
#         print(day)
#
#
# #     calender[i][i]
# #
# # print(calender)
#
# # for i in range(1, 13):
# #     month[i] = days[i]
# #     s
# #
# # print(day)