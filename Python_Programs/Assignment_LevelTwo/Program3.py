#count vowels

var = str(input("input the string:"))
count =0
vowels = ['a', 'e', 'i', 'o', 'u']

for ch in var.lower():
    if ch in vowels:
        count = count + 1
print("Number of vowels in the string:", count)



