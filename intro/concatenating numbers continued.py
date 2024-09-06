# number = input("Enter a number with three digits")

# first = number[0]
# second = number[1]
# third = number[2]

# total = int(first) + int(second) + int(third)

# message = "The sum of those digits is {}"

# print(message.format(total))




# User input
number = input("enter decimal")

#### Mathy bits
first = float(number) * 10
second = int(first % 10)

# Message, format(), print
message = "The first decimal digit is {}"

print(message.format(second))
