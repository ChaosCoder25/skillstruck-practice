# classmates = {
#     "Billy" : 8,
#     "Vance" : 12,
#     "Alice" : 10,
#     "Eliza" : 15,
#     "Xavier" : 6,
# }

# for x in classmates:
#     print(x)
# classmates = {
#     "Billy" : 8,
#     "Vance" : 12,
#     "Alice" : 10,
#     "Eliza" : 15,
#     "Xavier" : 6,
# }

# for x in classmates.values():
#     print(x)
# classmates = {
#     "Billy" : 8,
#     "Vance" : 12,
#     "Alice" : 10,
#     "Eliza" : 15,
#     "Xavier" : 6,
# }

# for x,y in classmates.items():
#     print(x,y)
# measurement = {"length": 10, "width": 5, "depth": 3}

# for x in measurement.values():
# 	print(x)
 
# first = int(input("Pick the height of box5"))		
# group = {
# 	"box1" : 5,
# 	"box2" : 2,
# 	"box3" : 10,
# 	"box4" : 3,
# 	"box5" : first
# }

# total_volume = 0 

# for x in group.values():
# 	volume =  25 * x
# 	total_volume =   volume + total_volume

# print(total_volume)
first = int(input("Pick a first number"))
second = int(input("Pick a second number"))			
group = {
	3 : 10,
	5 : 3,
	10 : 6,
	4 : 30,
	first : second
}

total = 0
for x,y in group.items():
	total =   total +(x*y)

print(total)