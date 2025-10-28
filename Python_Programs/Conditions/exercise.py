for i in range(5):
    print("Hello", i)

#understanding list
my_list = [10, 20, 30, "hello", True]

print(my_list[0])      # Access element → 10
print(my_list[-1])     # Last element → True

my_list.append(40)     # Add at end
my_list.insert(1, 15)  # Insert at index 1
my_list.remove(20)     # Remove specific value
print(len(my_list))    # Length of list
print(my_list)
print(my_list[-1])
print(my_list[-2])
print(my_list.pop())

#if conditions
x = 15

if x > 20:
    print("Greater than 20")
elif x == 15:
    print("Exactly 15")
else:
    print("Less than 20")
