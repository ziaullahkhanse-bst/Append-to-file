a = input("Enter a fileName: ")

b = input("Enter a text to add: ")

file = open(a, "a")

file.write(b + "\n")  # \n adds a new line

file.close()

print("Text added successfully!")
