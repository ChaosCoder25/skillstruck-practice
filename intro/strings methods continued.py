
number = int(input(" "))


if 100 <= number <= 999:
    
    digit1 = number // 100         
    digit2 = (number // 10) % 10   
    digit3 = number % 10           
    
    
    sum_of_digits = digit1 + digit2 + digit3
    
    
    print(f"The sum of those digits is {sum_of_digits}.")
else:
    print("Please enter a valid three-digit number.")
