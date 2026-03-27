def secondsFromYearStart(datetimeStr):
    datePart, timePart = datetimeStr.split()
    
    month, day, year = map(int, datePart.split('/'))
    hour, minute, second = map(int, timePart.split(':'))
    
    def isLeap(y):
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)
    
    daysInMonth = [31, 28 + isLeap(year), 31, 30, 31, 30,
                   31, 31, 30, 31, 30, 31]
    
    days = 0
    for i in range(month - 1):
        days += daysInMonth[i]
    
    days += (day - 1)
    
    totalSeconds = days * 24 * 3600
    totalSeconds += hour * 3600
    totalSeconds += minute * 60
    totalSeconds += second
    
    return totalSeconds


'''s = input()
print(secondsFromYearStart(s))'''
