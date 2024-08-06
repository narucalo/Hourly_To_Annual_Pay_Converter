import logging

# Hourly_to_Annual_Pay_Converter
# This program calculates the annual gross and net pay based on the hourly wage and applicable tax deductions.

def calculate_annual_pay(hourly_rate):
    """Calculate the gross annual pay assuming 40 hours per week and 52 weeks per year."""
    return hourly_rate * 40 * 52

def calculate_tax_deductions(annual_pay, status):
    """Apply tax deductions based on filing status."""
    # Placeholder for tax deduction amounts for different statuses in 2024
    tax_deductions = {
        "single": 12550,  # Assumed standard deduction for single filers
        "1_dependent": 12550 + 4300,  # Additional for one dependent
        "2_dependent": 12550 + 8600,  # Additional for two dependents
        "married_1_dependent": 25100 + 4300,  # Married filing jointly with one dependent
        "married_2_dependent": 25100 + 8600   # Married filing jointly with two dependents
    }
    
    # Calculate net annual pay after tax deduction
    deduction_amount = tax_deductions.get(status, 0)
    tax_rate = 0.22  # Assume a flat tax rate for simplicity
    taxable_income = max(0, annual_pay - deduction_amount)
    taxes_paid = taxable_income * tax_rate
    net_pay = annual_pay - taxes_paid
    return net_pay

def main():
    """Main function to handle user interaction and display results."""
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
    
    # Calculate and display results
    annual_gross_pay = calculate_annual_pay(hourly_rate)
    annual_net_pay = calculate_tax_deductions(annual_gross_pay, status)
    
    print(f"\nAnnual Gross Pay: ${annual_gross_pay:.2f}")
    print(f"Annual Net Pay after tax deductions: ${annual_net_pay:.2f}")

if __name__ == "__main__":
    main()
