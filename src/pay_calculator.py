import logging

# Hourly_to_Annual_Pay_Converter
# This program calculates the annual gross and net pay based on the hourly wage and tax deductions for Florida in 2024.

def calculate_annual_pay(hourly_rate):
    # Calculate the gross annual pay assuming 40 hours per week and 52 weeks per year.
    annual_pay = hourly_rate * 40 * 52
    return annual_pay

def calculate_tax_deductions(annual_pay, status):
    # Define tax deductions for Florida 2024 based on different family statuses
    # These values are placeholders. Replace them with the actual tax deduction values for 2024.
    tax_deductions = {
        "single": 1000,
        "1_dependent": 2000,
        "2_dependent": 3000,
        "married_1_dependent": 4000,
        "married_2_dependent": 5000
    }
    
    # Calculate net annual pay after tax deduction
    net_pay = annual_pay - tax_deductions.get(status, 0)
    return net_pay

def main():
    # User interface to gather inputs
    hourly_rate = float(input("Enter your hourly wage: "))
    print("\nChoose your filing status:")
    print("1 - Single")
    print("2 - Single with 1 dependent")
    print("3 - Single with 2 dependents")
    print("4 - Married with 1 dependent")
    print("5 - Married with 2 dependents")
    
    status_options = {
        "1": "single",
        "2": "1_dependent",
        "3": "2_dependent",
        "4": "married_1_dependent",
        "5": "married_2_dependent"
    }
    
    status_choice = input("Enter the number corresponding to your status: ")
    status = status_options.get(status_choice, "single")  # Default to single if invalid input
    
    # Calculations
    annual_gross_pay = calculate_annual_pay(hourly_rate)
    annual_net_pay = calculate_tax_deductions(annual_gross_pay, status)
    
    # Display results
    print(f"\nAnnual Gross Pay: ${annual_gross_pay:.2f}")
    print(f"Annual Net Pay after tax deductions: ${annual_net_pay:.2f}")

if __name__ == "__main__":
    main()
