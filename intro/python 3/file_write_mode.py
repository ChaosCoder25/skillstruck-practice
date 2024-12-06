# file = open("example.txt", "a")
# file.write("this is the new line we added!")
# file.close()
# file = open("example.txt", "w")
# file.write("this line replaces everything in this file!")
# file.close()
# file = open("new_document.txt", "w")
# file = open("example.txt", "w")
# file.write("In short, I love to code!")
# file.close()
# file = open("porcupine.txt", "w")
# file = open("example.txt", "w")
# file.write("Never mind")
# file.close()
# Step 1: Create an input and assign it to a variable named `answer`
answer = input("What would you like the greeting card to say? ")

# Step 2: Open a text file named 'report.txt' with the intent to write
with open("report.txt", "w") as file:
    # Step 3: Replace the contents of the file with whatever the user says
    file.write(answer)

# Step 4: Read the file to ensure it appended correctly
with open("report.txt", "r") as file:
    content = file.read()

# Display the content for confirmation
print("\nFile updated successfully! Here's what it says:")
print(content)
print(file.read())