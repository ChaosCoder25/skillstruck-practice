# n = 5
# list = []
# for i in range(n):
#     list.append(i)
# print(list)


# rows = 5
# cols = 5
# list = []
# for i in range(cols):
#     col = []
#     for j in range(rows):
#         col.append(j)
#         list.append(col)
# print(list)
# list = ["hello" for i in range(5)]
# print(list)
# rows = int(input("How many rows do you want?"))
# mylist = [1, 2, 3, 4, 5]
# list = [[(j*rows) for j in mylist] for i in range(rows)]

# print(list)
# Create a variable for the number of rows
rows = 3

# Create a list of 5 strings
pets = ["dog", "cat", "fish", "bird", "hamster"]

# Generate a 2D list using a one-line nested for loop
pet_matrix = [[pet for pet in pets] for _ in range(rows)]

# Print the 2D list
print(pet_matrix)
