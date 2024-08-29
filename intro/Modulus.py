# number = int(input("Pick a number that is two digits"))
# tens = number // 10
# ones = number % 10
# print(tens , ones)

number = int(input("Pick a number that is 10 or greater"))
last_two_digits = number % 100
print(last_two_digits)