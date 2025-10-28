# Input two strings
str1 = input("Enter the first string: ").lower()   # convert to lowercase
str2 = input("Enter the second string: ").lower()

# Sort both strings
sorted_str1 = sorted(str1)
sorted_str2 = sorted(str2)

print(sorted_str1)
print(sorted_str2)

# Compare the sorted strings
if sorted_str1 == sorted_str2:
    print("The strings are Anagrams")
else:
    print("The strings are Not Anagrams")
