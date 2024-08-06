# main.py
# This module handles user interaction and integrates the pay and tax calculation modules.

from pay_calculator import calculate_annual_pay
from tax_deductions import calculate_tax_deductions

def main():
    hourly_rate = float(input("Enter your hourly wage: "))
    print("\nChoose your filing status:")
    status_options = ["Single", "Single with 1 dependent", "Single with 2 dependents", 
                      "Married with 1 dependent", "Married with 2 dependents"]
    for i, status in enumerate(status_options, 1):
        print(f"{i} - {status}")
    
    status_choice = int(input("Enter the number corresponding to your status: ")) - 1
    status = status_options[status_choice] if status_choice < len(status_options) else "Single"
    
    gross_pay = calculate_annual_pay(hourly_rate)
    net_pay = calculate_tax_deductions(gross_pay, status.lower().replace(" ", "_"))
    
    print(f"\nAnnual Gross Pay: ${gross_pay:.2f}")
    print(f"Annual Net Pay after tax deductions: ${net_pay:.2f}")

if __name__ == "__main__":
    main()
