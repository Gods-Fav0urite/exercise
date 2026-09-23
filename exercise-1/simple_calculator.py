try:
    first_number = float(input("First number: "))
except ValueError:
    print("Invalid number input")
    exit()

operator = input("Operator: ")

try:
    second_number = float(input("Second number: "))
except ValueError:
    print("Invalid number input")
    exit()

if operator == "*":
    result = first_number * second_number
    print(f"Result: {result}")
elif operator == "+":
    result = first_number + second_number
    print(f"Result: {result}")
elif operator == "-":
    result = first_number - second_number
    print(f"Result: {result}")
elif operator == "/":
    if second_number == 0:
        print("Cannot divide by zero")
    else:
        result = first_number / second_number
        print(f"Result: {result}")
elif operator == "%":
    if second_number == 2:
        print("Invalid operator")
    else:
        result = first_number % second_number
        print(f"Result: {result}")

