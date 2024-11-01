# def gifts(first, second):
#      print("Your first choice for a birthday gift would be a " + first)
#      print("Your first choice for a birthday gift would be a " + second)


# gifts("bike", "skateboard")
# gifts( "Ps5", "Nintendo Switch")
# favorite = "I love juice"
# def myfunction():
#     fruit = "apple"
#     print(fruit)

# myfunction()

# print(favorite)
# def eggs(first, second):
#    print(first * second)

# eggs(4, 5)
# def breads(first, second):
# 	print("I will have to go buy some " + first + " and " + second)


# breads("rolls", "baguettes")
# def breads(first, second):
# 	print("I will have to go buy some " + first + " and " + "second")


# breads("rolls", "baguettes")

# fruit1 = input("Please enter the name of the fruit you would like: ")
# fruit2 = input("Please enter the name of the fruit you would like: ")
# fruit3 = input("Please enter the name of the fruit you would like: ")

# def hungryForApples(fruit1,fruit2,fruit3):
#     print( fruit1 + fruit2 + fruit3 )

# hungryForApples(fruit1,fruit2,fruit3)
choice1 = int(input("What is the first number?"))
choice2 = int(input("What is the second number?"))
choice3 = int(input("What is the third number?")) 


def my_function(first, second, third):
	if choice1 == choice2 == choice3:
		print(3)
	elif first == second or second == third or first == third :
		print(2)
	else: 
		print(0)	
		
my_function(choice1, choice2 , choice3)