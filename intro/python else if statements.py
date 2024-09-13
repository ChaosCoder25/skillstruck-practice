# vacation = "amusement_park"

# if vacation =="beach":
#     print("you love the ocean")
# elif vacation == "amusement_park":
#     print("you like to ride roller coasters")
# elif vacation == "mountains":
#         print("you love to get up and away")
# else:
#     print("you like unique vacation destinations")
#coins = 20
# if coins > 20: print("you have more than enough to by a puppy")
#elif coins == 20: print("you have exactly enough to buy a puppy")

# Function to determine if a year is a leap year
def check_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap"
            else:
                return "Common"
        else:
            return "Leap"
    else:
        return "Common"

# Input: Receive a year from the user
year = int(input("Enter a year: "))

# Output: Determine and print if it's a Leap or Common year
result = check_leap_year(year)
print(result)
