FAHRENHEIT_TO_CELSIUS_FACTOR = (5 / 9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9 / 5)


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    while True:
        try:
            temp = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit == 'C':
                converted_temp = convert_to_fahrenheit(temp)
                print(f"{temp}°C is {converted_temp:.2f}°F")
            elif unit == 'F':
                converted_temp = convert_to_celsius(temp)
                print(f"{temp}°F is {converted_temp:.2f}°C")

            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

        except ValueError as e:
            if str(e).startswith("could not convert string to float"):
                print("Invalid temperature. Please enter a numeric value.")
            else:
                print(f"Error: {e}")

        cont = input("Do you want to perform another conversion? (y/n): ").strip().lower()
        if cont != 'y':
            break


if __name__ == "__main__":
    main()
