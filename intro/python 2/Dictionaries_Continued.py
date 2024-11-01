
# classmates = {
# 	"tim" : 8,
# 	"ralph" : 15,
# 	"tom" : 10,
# 	"benson" : 6,
# 	"skips" : 12,
# }
# if "ralph" in classmates:
#     print("ralph is in your dictionary")
# classmates = {
# 	"tim" : 8,
# 	"ralph" : 15,
# 	"tom" : 10,
# 	"benson" : 6,
# 	"skips" : 12,
# }
# if "thomas" not in classmates:
#     print("thomas is in your dictionary")
# garden = ["pumpkins", "squash", "corn", "tomatoes"]

# garden_dictionary = dict.fromkeys(garden, "Harvested")

# print(garden_dictionary)
# coins = {
#    		 "pennies" : 1,
#    		 "nickels": 5,
#   		 "dimes": 10,
#   		 "quarters": 25,
# }

# print(coins)
# coins["silver dollar"] = 5
# coins.pop("pennies")
# print("updated dictionary:",coins)
# print(len(coins))
# dictionary = {
# 	1: "bicycle",
# 	2: "soccer balls",
# 	3: "piano books"
# }

# dictionary[4] = input("What do you have 4 of?")
# dictionary[5] = input("What do you have 5 of?")
# dictionary[6] = input("What do you have 6 of?")
						  
# print(dictionary)
work = {

	"Monday": 3,
	"Tuesday": 4, 
	"Wednesday": 2,
	"Thursday": 1, 
	"Friday": 1, 
	
}

work["Saturday"] = 4
work.pop("Wednesday")
print(len(work))

if "Friday" in work:
	print("Friday is in work")

print(work)