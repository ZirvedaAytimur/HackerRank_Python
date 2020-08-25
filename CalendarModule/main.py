import calendar

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

day = list(map(int, input().split()))

print(days[calendar.weekday(day[2], day[0], day[1])])