def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            print("Cannot divide by zero.")
            return None
        else:
            return num1 / num2
    else:
        return f"Invalid operation '{operation}'. Please choose from 'add', 'subtract', 'multiply', 'divide'."
