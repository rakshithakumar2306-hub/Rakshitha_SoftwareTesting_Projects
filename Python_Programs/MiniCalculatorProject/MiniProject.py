# --- Calculator Functions ---
def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error: Divide by zero"
def power(a, b): return a ** b

# --- Collections to store results ---
results_list = []          # to keep all results (with duplicates)
operations_tuple = ()      # to track operations performed
unique_results = set()     # to remove duplicates later

while True:
    print("\n--- Calculator Menu ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    if choice == "6":
        print("Exiting calculator...")
        break

    # validate numeric input
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("❌ Invalid input, please enter numbers only.")
        continue

    # perform operation
    if choice == "1":
        result = add(a, b); operation = "Add"
    elif choice == "2":
        result = subtract(a, b); operation = "Subtract"
    elif choice == "3":
        result = multiply(a, b); operation = "Multiply"
    elif choice == "4":
        result = divide(a, b); operation = "Divide"
    elif choice == "5":
        result = power(a, b); operation = "Power"
    else:
        print("❌ Invalid choice! Try again.")
        continue

    print(f"✅ {operation} result = {result}")

    # store results in collections
    results_list.append(result)
    operations_tuple += (operation,)
    if isinstance(result, (int, float)):  # only add numeric results to set
        unique_results.add(result)

# --- After user exits, show summary ---
print("\n--- Calculator Summary ---")
print("All results (list):", results_list)
print("Operations performed (tuple):", operations_tuple)
print("Unique results (set):", unique_results)

if unique_results:  # avoid error if empty
    summary = {
        "max_result": max(unique_results),
        "min_result": min(unique_results)
    }
    print("Summary dictionary:", summary)
