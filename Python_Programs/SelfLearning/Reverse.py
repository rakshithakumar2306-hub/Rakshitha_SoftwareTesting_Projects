"""
var= str(input("Enter the string:"))
rev_var = var[::-1]
print("The reversed string is:",rev_var)
"""

var= str(input("Enter the string:"))
rev_str=""
for i in range(len(var)-1,-1,-1):
    rev_str+=var[i]
print("The reversed string is:",rev_str)


