"""
6. Write a Java / Pyhtonprogram to check whether a given string ends with the contents of another string
Sample Output:
"Python Exercises" ends with "se"? false
"Python Exercise" ends with "se"? true
"""

str1="Python Exercises"
str2="se"
str3="Python Exercise"

print(f'"{str1}" ends with "{str2}"', str1.endswith(str2))
print(f'"{str3}" ends with "{str2}"', str3.endswith(str2))