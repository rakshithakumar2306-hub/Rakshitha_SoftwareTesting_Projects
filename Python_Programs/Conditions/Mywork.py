"""
n=int(input("Enter the number"))

for i in range(1,11):
  print(f" {n} x {i} = {n*i}")
"""
print("even numbers")
for i in range(1,101):
    if i%2==0:
        print(i, end=" ")

print("\nodd numbers")
for i in range(1, 101):
   if i%2==1:
       print(i, end=" ")
