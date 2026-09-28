def continuous_calculator():
    current_total = 0.0
    history = []  
    print("Continuous Calculator Started.")
    print("Inputs should be: an operator then a number (e.g; '+ 5') or 'undo'.")
    print(f"Starting Total: {current_total}")
    

    while True:
        user_input = input("Enter operation: ").strip()

        if user_input.lower() == "undo":
            if len(history) > 0:
                current_total = history.pop()  
                print(f"Result: {current_total}")
            else:
                print("Error: Nothing to undo.")
            continue  
        parts = user_input.split()
        if len(parts) != 2:
            print("Invalid format, Please enter an operator followed by a number.")
            continue

        operator = parts[0]
        number_text = parts[1]

        if operator not in ['+', '-', '*', '/']:
            print(f"Error: '{operator}' is not a valid operator.")
            continue

        try:
            number = float(number_text)
        except ValueError:
            print(f"Error: '{number_text}' is not a valid floating-point number.")
            continue

        if operator == '/' and number == 0.0:
            print("Error: Division by zero is not allowed.")
            continue

        history.append(current_total)

        if operator == '+':
            current_total += number
        elif operator == '-':
            current_total -= number
        elif operator == '*':
            current_total *= number
        elif operator == '/':
            current_total /= number

        print(f"Result: {current_total}")

if __name__ == "__main_":
    continuous_calculator()
