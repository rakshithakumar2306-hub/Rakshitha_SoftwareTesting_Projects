"""
9. Write a Java / Pyhton program to print after removing duplicates from a given string
Sample Output:
The given string is: w3resource
After removing duplicates characters the new string is: w3resouc
"""

Original_string="w3resource"
New_string=" "

for char in Original_string:
    if char not in New_string:
        New_string += char
print("the given string is:",Original_string)
print("After removing duplicates characters the new string is:", New_string)
