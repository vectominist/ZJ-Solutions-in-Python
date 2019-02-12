import sys

# Calculate number of days between two days
LeapYear = 366
AvgYear  = 365

days_of_year = [0] * 10000
for i in range(10000):
    if i % 400 == 0:
        days_of_year[i] = LeapYear
    elif i % 100 == 0:
        days_of_year[i] = AvgYear
    elif i % 4 == 0:
        days_of_year[i] = LeapYear
    else:
        days_of_year[i] = AvgYear
    
days_of_month_Avg  = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_of_month_Leap = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


for s in sys.stdin:
    num1 = s.split()
    s = sys.stdin.readline()
    num2 = s.split()
    year  = [int(num1[0]), int(num2[0])]
    month = [int(num1[1]), int(num2[1])]
    day   = [int(num1[2]), int(num2[2])]
    # Let [0] < [1]
    if (year[0] > year[1]) or \
        ((year[0] == year[1]) and (month[0] > month[1])) or \
        ((year[0] == year[1]) and (month[0] == month[1]) and (day[0] > day[1])):
        year.reverse()
        month.reverse()
        day.reverse()
    
    ans = 0
    if year[0] != year[1]:
        for i in range(year[0] + 1, year[1]):
            ans += days_of_year[i]
    
    daysM = [day[0], day[1]]
    for i in range(2):
        for m in range(1, month[i]):
            if days_of_year[year[i]] == LeapYear:
                daysM[i] += days_of_month_Leap[m]
            else:
                daysM[i] += days_of_month_Avg[m]
    #print('%d %d %d' % (ans, daysM[0], daysM[1]))
    if year[0] == year[1]:
        print(daysM[1] - daysM[0])
    else:
        print(ans + days_of_year[year[0]] - daysM[0] + daysM[1])
