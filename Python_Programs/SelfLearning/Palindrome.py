org_str=input("enter the string")
print("The original string is:",org_str)
rev_str=""

for i in range(len(org_str)-1,-1,-1):
    rev_str+=org_str[i]
print("The reversed string is:",rev_str)

if org_str==rev_str:
    print("The string is palindrome")
else:
    print("The string is not palindrome")