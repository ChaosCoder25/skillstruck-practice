# classmates = {
#     "Billy" : 8,
#     "Vance" : 12,
#     "Alice" : 10,
#     "Eliza" : 15,
#     "Xavier" : 6,
# }

# for x in classmates:
#     if x == "Eliza":
#         print("This person wants to be anonymous")
#     else:
#             print(x)
# periods = int(input("How many class periods do you have?"))
# schedule = {}
# for i in range(periods):
#     subject = input("What subject?")
#     num_people = input("How many people are in your  " + subject + " class?")
#     if subject not in schedule:
#         schedule[subject] = num_people
# print(schedule)
# ride = {
# "tommy": 120,
# "angel": 50,
# "charlie": 121,
# "jorden": 40,
# "noah": 99,
# }

# for x in ride.values():
#     if x >= 100:
#         print(" This person is tall enough to ride.")
#     else:   
#         print("This person is too short to ride.")

# dictionary = {
#   7: "first",
#   3: "second",
#   4: "third",
#   8: "fourth",
#   9: "fifth",
# }

# my_list = [int(n) for n in input().split()]

# for x in my_list:
#     if x in dictionary:
#         print("Yes")
#     else:
#         print("No")
# Step 1: Get the total number of data points
num_data_points = int(input("Enter the number of vote data points: "))

# Step 2: Initialize an empty dictionary to store the candidates and their vote totals
vote_tally = {}

# Step 3: Loop through the data points to collect and consolidate votes
for _ in range(num_data_points):
    # Get the candidate's name and the number of votes they received
    name = input("Enter candidate's name: ")
    votes = int(input("Enter number of votes: "))
    
    # If the candidate is already in the dictionary, add the votes to their existing total
    # Otherwise, add the candidate to the dictionary with the received votes
    if name in vote_tally:
        vote_tally[name] += votes
    else:
        vote_tally[name] = votes

# Step 4: Print the final vote tally dictionary
print(vote_tally)
