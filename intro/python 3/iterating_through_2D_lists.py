# my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]
# rows = 4
# cols = 3

# for i in range(rows):
#     for j in range(cols):
#         my_list[i][j] = my_list[i][j] * 2

# print(my_list)

# my_list = [["dog", "cat", "frog"], ["shark", "squid", "whale"], ["deer", "fox", "badger"]]
# rows = 3
# cols = 3

# for i in range(rows):
#     for j in range(cols):
#         my_list[i][j] = my_list[i][j] + " is awsome"

# print(my_list)


# my_list = [[40, 45, 50], [6, 7, 8], [100, 200, 300], [50, 60, 70], [9, 0, 1]]
# rows = 5
# cols = 3

# for i in range(rows):
#     for j in range(cols):
#         my_list[i][j] = my_list[i][j] + 3

# print(my_list)

# my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]
# rows = 4
# cols = 3

# # Ask the user what to multiply each value by
# answer = int(input("What do you want to multiply by? "))

# # Multiply each element in the 2D list
# for i in range(rows):
#     for j in range(cols):
#         my_list[i][j] = my_list[i][j] * answer

# # Print the updated list
# print(my_list)
x = int(input("What is the first number?"))
y = int(input("What is the second number?"))
z = int(input("What is the third number?"))


my_list = [[0, 1, x ], [10, 15, y], [100, 200, 300], [5, 6, z]]
rows = 4
cols = 3

largest = my_list[0][0]

for i in range(rows):
    for j in range(cols):
        if my_list[i][j] > largest:
            largest = my_list[i][j]

print(largest)
