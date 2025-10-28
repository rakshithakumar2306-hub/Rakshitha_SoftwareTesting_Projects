#smallest among 3 numbers

n1 = float(input ("Input the first number: "))
n2 = float(input ("Input the second number: "))
n3 = float(input ("Input the third number: "))

if n1<n2 and n1<n3:
    print("The smallest value is:",n1)
elif n2<n1 and n2<n3:
    print("The smallest value is:",n2)
else:
    print("The smallest value is:",n3)


#print("The smallest value is:", min(n1,n2,n3))