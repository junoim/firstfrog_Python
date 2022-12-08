#How many seconds are in a year? 

print("How many seonds are there in a year??")
print()
print()
days_in_year = 365
days_in_leapyear = 366
hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60
print("a year might as well be a leap year which would impact the overall seconds in the year to prevent that.....")
print()
year = int(input("which year are you looking for?: "))
if year % 4 == 0 :
  leapyear_result = days_in_leapyear * hours_in_day * minutes_in_hour * seconds_in_minute
  print("This is a Leap year!, it has!",leapyear_result,"seconds")
else:
  result = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute
  print("This year has,",result,"seconds")
