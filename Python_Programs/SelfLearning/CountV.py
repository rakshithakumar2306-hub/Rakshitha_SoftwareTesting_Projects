"""
count vowels and consonants
"""
var=input("enter string:")
vowels=['a','e','i','o','u','A','E','I','O','U']
vowelsc=0
consonants=0
for i in range(len(var)):
    if var[i].isalpha():
        if var[i] in vowels:
         vowelsc+=1
        else:
          consonants+=1
print("The number of vowels is:",vowelsc)
print("The number of consonants is:",consonants)


