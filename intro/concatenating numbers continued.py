number_of_miles =  int(input("Enter the number of miles your car can drive in a day: "))
total_miles = int(input("Enter the total number of miles to get to your destination: "))

days_needed = total_miles // miles_per_day
if total_miles % miles_per_day != 0:
    days_needed +  1
print(miles_per_day.format,"It will take your car {days_needed} days to make that trip.")    