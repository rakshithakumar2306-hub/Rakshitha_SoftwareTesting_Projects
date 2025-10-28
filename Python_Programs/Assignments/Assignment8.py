"""
8. Write a Java / Pyhton program to replace a specified character with another character
- Sample Output:
   - Original string: The quick brown fox jumps over the lazy dog.
   - New String: The quick brown fox jumps over the lazy fog.
"""
string1="The quick brown fox jumps over the lazy dog."

string2 = string1.replace('d','f')
print(f'Original string: {string1}')
print(f'New string: {string2}')

string1="The quick brown fox jumps over the lazy dog."
string2 = string1.replace('dog','fog')
print(f'Original string: {string1}')
print(f'New string: {string2}')

