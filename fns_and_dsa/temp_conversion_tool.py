FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    while True:
        try:
            temp_input = input("Enter the temperature to convert (or 'q' to quit): ")
            if temp_input.strip().lower() == 'q':
                print("Exiting the program.")
                break

            temp = float(temp_input)
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'C':
                converted_temp = convert_to_fahrenheit(temp)
                print(f"{temp}°C is {converted_temp:.2f}°F")
            elif unit == 'F':
                converted_temp = convert_to_celsius(temp)
                print(f"{temp}°F is {converted_temp:.2f}°C")
            else:
                raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
        except ValueError as e:
            print(f"Invalid input. Please enter a numeric value for temperature and a valid unit. Error: {e}")

        cont = input("Do you want to perform another conversion? (y/n): ").strip().lower()
        if cont != 'y':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
