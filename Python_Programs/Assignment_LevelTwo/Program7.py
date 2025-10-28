#accept five numbers from user and find sum and average
"""
n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
n5=int(input())
print("The numbers are:",n1,n2,n3,n4,n5)
sum=n1+n2+n3+n4+n5
average=sum/5
print("The sum of 5 number's is:",sum)
print("The average of 5 number's is:",average)

"""
print("Input the 5 numbers :")
nums = []

for i in range(5):
    n = int(input())
    nums.append(n)

total = sum(nums)
average = total / len(nums)

print("The sum of 5 no is :", total)
print("The Average is :", average)


