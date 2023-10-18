import calendar as cal
try:
    day = int(input("Enter a day of the month: "))
    month = int(input("Enter month of the year: "))
    year = int(input("Enter the year: "))
    dayN = cal.weekday(year, month, day)
    print(cal.day_name[dayN])
except:
    print("Please make sure you gave the current values")