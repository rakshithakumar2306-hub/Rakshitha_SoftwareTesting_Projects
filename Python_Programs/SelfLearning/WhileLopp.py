"""
i=1
while i<=20:
    print(i)
    i = i + 1
"""
"""
i=10
while i<=50:
    if i%2==0:
        print(i)
    i=i+2
"""

total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num

print("Sum of all numbers entered:", total)



secret_number = 7

while True:
    guess = int(input("Guess the secret number (1-10): "))
    if guess == secret_number:
        print("Congratulations! You guessed it right.")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

