file - open("example.txt", "a")
file.write("This is the new line we added!")
file.close()

file = open("example.txt", "r")
print(file.read())