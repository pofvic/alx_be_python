
def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

monthly_income = get_integer_input("Enter your monthly income: ")
monthly_expenses = get_integer_input("Enter your total monthly expenses: ")

monthly_savings = monthly_income - monthly_expenses

annual_savings = monthly_savings * 12 * 1.05

print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings:.2f}.")
