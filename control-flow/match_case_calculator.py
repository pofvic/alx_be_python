first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

operation = input("(+, -, *, /): ")


match operation:
    case "+":
        result = first_number + second_number
    case "-":
        result = first_number - second_number
    case '*':
        result = first_number * second_number
    case "/":
        result = first_number / second_number

        if second_number == 0:
            result = first_number / second_number
        else:
            result = "Error: Division by zero is not allowed"

    case _:
        result = "Error: Invalid operations"


print("The result is", result)

