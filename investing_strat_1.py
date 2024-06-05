# investment_strat_1.py

import matplotlib.pyplot as plt

def get_user_input(prompt, default=0):
    try:
        return float(input(prompt) or default)
    except ValueError:
        print("Invalid input. Please enter a numeric value.") 
        return get_user_input(prompt, default)

# User inputs
user_income = get_user_input("Enter your annual work income: ")
income = user_income
user_expense = get_user_input("Enter your annual expenses: ")
total_invest = get_user_input("Enter your current total investments: ")
years = int(get_user_input("Enter the number of years for the program: ", 1))

# Constants
EXPENSE_INFLATION_RATE = 0.07
INVESTMENT_RETURN_RATE = 0.08
SALARY_HIKE_RATE = 0.1
SALARY_HIKE_FREQUENCY = 3  # years

# Data storage for plotting
return_value_data = []
expense_data = []
year_data = []

# Functions
def calculate_annual_expense(expense, year):
    return expense * (1 + EXPENSE_INFLATION_RATE) ** year

def for_investment_amount(income, expense):
    after_cut = round(income - expense)
    investment_percent = (after_cut / user_income) * 100
    for_invest = round((after_cut * investment_percent) / 100)
    return for_invest

def market_value(value, total_invest):
    total_invest += value
    return total_invest + (INVESTMENT_RETURN_RATE * total_invest)

def salary_hike(income, year):
    if year % SALARY_HIKE_FREQUENCY == 0 and year != 0:  # Salary hike every 3 years, but not in the first year
        income += SALARY_HIKE_RATE * income
    return income 

# Main calculation loop
for i in range(years):
    annual_expense = calculate_annual_expense(user_expense, i)
    for_invest = for_investment_amount(user_income, annual_expense)
    return_value = round(market_value(for_invest, total_invest), 2)
    user_income += return_value * 0.1  # Add 10% of return value to income

    print(f"Year {i+1}:")
    print(f"Investment strategy: Allocate ${for_invest}. Withdraw ${round(return_value * 0.1, 2)} for other uses. Reinvest the rest to earn an 8% return.")
    print(f"End of Year {i+1} portfolio value: ${return_value}")
    print(" ")

    total_invest = return_value
    return_value_data.append(return_value)
    expense_data.append(annual_expense)
    year_data.append(i + 1)

    user_income = salary_hike(user_income, i)

# Plotting results if the user wants a graph
graph = input("Do you want a graph? (Y/N): ").strip().lower()

if graph == 'y':
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

    # Plotting Year vs Return Value
    ax1.plot(year_data, return_value_data, marker='o', linestyle='-', color='g')
    ax1.set_title('Year vs Return Value')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Return Value')
    ax1.grid(True)

    # Plotting Year vs Expense
    ax2.plot(year_data, expense_data, marker='o', linestyle='-', color='b')
    ax2.set_title('Year vs Expense')
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Expense')
    ax2.grid(True)

    plt.tight_layout()
    plt.show()
