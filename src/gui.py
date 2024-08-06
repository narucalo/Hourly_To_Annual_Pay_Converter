# gui.py
# This module sets up the GUI for the Hourly_to_Annual_Pay_Converter using tkinter.

import logging



import tkinter as tk
from tkinter import ttk
from pay_calculator import calculate_annual_pay
from tax_deductions import calculate_tax_deductions

class PayCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hourly to Annual Pay Converter')
        self.geometry('400x300')  # Set the size of the GUI window

        # Create and pack the widgets
        self.create_widgets()

    def create_widgets(self):
        # Hourly wage input
        self.hourly_rate_label = ttk.Label(self, text="Enter your hourly wage:")
        self.hourly_rate_label.pack(pady=(20, 5))
        
        self.hourly_rate_entry = ttk.Entry(self)
        self.hourly_rate_entry.pack(pady=5)
        
        # Filing status selection
        self.status_label = ttk.Label(self, text="Select your filing status:")
        self.status_label.pack(pady=(20, 5))
        
        self.statuses = ["Single", "Single with 1 dependent", "Single with 2 dependents",
                         "Married with 1 dependent", "Married with 2 dependents"]
        self.status_var = tk.StringVar()
        self.status_menu = ttk.OptionMenu(self, self.status_var, self.statuses[0], *self.statuses)
        self.status_menu.pack(pady=5)
        
        # Calculate button
        self.calculate_button = ttk.Button(self, text="Calculate", command=self.calculate_pay)
        self.calculate_button.pack(pady=(20, 5))
        
        # Results display
        self.result_label = ttk.Label(self, text="")
        self.result_label.pack(pady=(20, 5))

    def calculate_pay(self):
        # Get inputs
        hourly_rate = float(self.hourly_rate_entry.get())
        status = self.status_var.get().lower().replace(" ", "_")
        
        # Calculate pays
        gross_pay = calculate_annual_pay(hourly_rate)
        net_pay = calculate_tax_deductions(gross_pay, status)
        
        # Display results
        self.result_label.config(text=f"Annual Gross Pay: ${gross_pay:.2f}\n"
                                      f"Annual Net Pay after tax deductions: ${net_pay:.2f}")

def run_app():
    app = PayCalculatorApp()
    app.mainloop()

if __name__ == "__main__":
    run_app()
