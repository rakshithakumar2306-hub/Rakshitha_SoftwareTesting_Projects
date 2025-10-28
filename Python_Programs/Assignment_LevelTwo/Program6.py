#print greatest of 3 numbers by taking 3 numbers from user

n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
n3=int(input("Enter the third number: "))

if n1>n2 and n1>n3:
    print("The greatest:",n1)
elif n2>n1 and n2>n3:
    print("The greatest:",n2)
else:
    print("The greatest:",n3)
