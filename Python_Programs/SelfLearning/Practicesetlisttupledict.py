fruits = ["Apple", "Banana", "Cherry", "Grapes", "Orange"]
# Your code here
print(fruits[1])
fruits.append("Avacado")
print(fruits)
fruits.remove("Apple")
print(fruits)
print(len(fruits))
fruits.insert(2, "Mango")
print(fruits)


colors = ("Red", "Green", "Blue", "Yellow")
# Your code here
print(colors[0])
print(colors[3])
#colors.insert(1,"Purple")# we will get error as tuples are immutatble
print(colors)

numbers = {1, 2, 2, 3, 4, 4}
# Your code here
print(numbers)
numbers.add(5)
print(numbers)
numbers.remove(3)
print(numbers)

student = {"name": "Riya", "age": 16, "grade": "B"}
# Your code here
print(student["name"])
student["grade"]="A+"
student["roll_no"]= "101"
print(student)
del student["age"]
print(student)

#5Combined Practice
my_list=[85,90,78,92,88]
my_list=set(my_list)
print(my_list)
print(max(my_list))
print(min(my_list))
results ={"max_score":max(my_list), "min_score":min(my_list)}
print(results)
