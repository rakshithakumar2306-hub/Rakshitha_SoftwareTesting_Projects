var = input("Enter the string: ")

for char in var:
    if var.count(char) == 1:
        print("First non-repeating character is:", char)
        break
