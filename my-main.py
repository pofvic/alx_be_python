from arithmetic_operations import perform_operation


def main():
    print('pof calculator')
    first_number = float(input("enter first number"))
    second_number = float(input("enter second number"))
    operations = input("choose an operations (add, subtract, divide, multiply").strip().lower()

    result = perform_operation(first_number, second_number, operations)
    print(f"Result {result}")


if __name__ == "_main_":
    main()