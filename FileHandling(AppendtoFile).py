a = input("Enter a fileName: ")

b = input("Enter a text to add: ")

# Open file in append mode
file = open(a, "a")

# Write text to file
file.write(b + "\n")  # \n adds a new line

# Close file
file.close()

# Success message
print("Text added successfully!")
