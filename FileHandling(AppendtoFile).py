a = input("Enter a fileName: ")

b = input("Enter a text to add: ")

file = open(a, "a")

file.write(b + "\n")  # \n adds a new line

# Close file
file.close()

# Success message
print("Text added successfully!")
