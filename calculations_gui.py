import tkinter as tk
from tkinter import messagebox
import math
from datetime import datetime

def calculate_average_grades(grades):
    """Calculate average grade."""
    if not grades:
        return 0
    return sum(grades) / len(grades)

def calculate_tax(income, tax_rate):
    """Calculate tax amount."""
    return income * (tax_rate / 100)

def calculate_work_hours(start_time, end_time):
    """Calculate work hours between two times."""
    fmt = "%H:%M"
    start = datetime.strptime(start_time, fmt)
    end = datetime.strptime(end_time, fmt)
    return (end - start).seconds / 3600  # hours

def calculate_circle_area(radius):
    """Calculate area of a circle."""
    return math.pi * (radius ** 2)

def calculate_bmi(weight, height):
    """Calculate Body Mass Index (BMI)."""
    return weight / (height ** 2)

def calculate_simple_interest(principal, rate, time):
    """Calculate simple interest."""
    return principal * (rate / 100) * time

def currency_conversion(amount, rate):
    """Convert currency using the given rate."""
    return amount * rate

def show_average_grades():
    """Handle average grade calculation."""
    try:
        grades_input = grades_entry.get().strip().split(',')
        grades = [float(g) for g in grades_input]
        average = calculate_average_grades(grades)
        messagebox.showinfo("Average Grade", f"The average grade is: {average:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid grades.")

def show_tax():
    """Handle tax calculation."""
    try:
        income = float(income_entry.get())
        tax_rate = float(tax_rate_entry.get())
        tax = calculate_tax(income, tax_rate)
        messagebox.showinfo("Tax Calculation", f"The tax amount is: {tax:.2f} Euros")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid income and tax rate.")

def show_work_hours():
    """Handle work hours calculation."""
    try:
        start_time = start_time_entry.get()
        end_time = end_time_entry.get()
        hours = calculate_work_hours(start_time, end_time)
        messagebox.showinfo("Work Hours", f"You worked for: {hours:.2f} hours.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid start and end times in HH:MM format.")

def show_circle_area():
    """Handle circle area calculation."""
    try:
        radius = float(circle_radius_entry.get())
        area = calculate_circle_area(radius)
        messagebox.showinfo("Circle Area", f"The area of the circle is: {area:.2f} square meters.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid radius.")

def show_bmi():
    """Handle BMI calculation."""
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = calculate_bmi(weight, height)
        messagebox.showinfo("BMI Calculation", f"Your BMI is: {bmi:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid weight and height.")

def show_simple_interest():
    """Handle simple interest calculation."""
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())
        interest = calculate_simple_interest(principal, rate, time)
        messagebox.showinfo("Simple Interest", f"The simple interest is: {interest:.2f} Euros")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid principal, rate, and time.")

def show_currency_conversion():
    """Handle currency conversion."""
    try:
        amount = float(amount_entry.get())
        rate = float(conversion_rate_entry.get())
        converted_amount = currency_conversion(amount, rate)
        messagebox.showinfo("Currency Conversion", f"The converted amount is: {converted_amount:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid amount and conversion rate.")

def guess_number_game():
    """A simple number guessing game."""
    import random
    number = random.randint(1, 100)
    
    def check_guess():
        try:
            guess = int(guess_entry.get())
            if guess < number:
                messagebox.showinfo("Guess Result", "Too low! Try again.")
            elif guess > number:
                messagebox.showinfo("Guess Result", "Too high! Try again.")
            else:
                messagebox.showinfo("Guess Result", "Congratulations! You guessed it!")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number.")

    game_window = tk.Toplevel(root)
    game_window.title("Guess the Number")
    tk.Label(game_window, text="Guess a number between 1 and 100:").pack()
    guess_entry = tk.Entry(game_window)
    guess_entry.pack()
    tk.Button(game_window, text="Check Guess", command=check_guess).pack()

# Create the main window
root = tk.Tk()
root.title("Comprehensive Calculation Program")

# Create widgets for average grade calculation
tk.Label(root, text="Enter grades (comma separated):").grid(row=0, column=0)
grades_entry = tk.Entry(root)
grades_entry.grid(row=0, column=1)
tk.Button(root, text="Calculate Average Grade", command=show_average_grades).grid(row=0, column=2)

# Create widgets for tax calculation
tk.Label(root, text="Income:").grid(row=1, column=0)
income_entry = tk.Entry(root)
income_entry.grid(row=1, column=1)
tk.Label(root, text="Tax Rate (%):").grid(row=2, column=0)
tax_rate_entry = tk.Entry(root)
tax_rate_entry.grid(row=2, column=1)
tk.Button(root, text="Calculate Tax", command=show_tax).grid(row=1, column=2, rowspan=2)

# Create widgets for work hours calculation
tk.Label(root, text="Start Time (HH:MM):").grid(row=3, column=0)
start_time_entry = tk.Entry(root)
start_time_entry.grid(row=3, column=1)
tk.Label(root, text="End Time (HH:MM):").grid(row=4, column=0)
end_time_entry = tk.Entry(root)
end_time_entry.grid(row=4, column=1)
tk.Button(root, text="Calculate Work Hours", command=show_work_hours).grid(row=3, column=2, rowspan=2)

# Create widgets for circle area calculation
tk.Label(root, text="Circle Radius:").grid(row=5, column=0)
circle_radius_entry = tk.Entry(root)
circle_radius_entry.grid(row=5, column=1)
tk.Button(root, text="Calculate Circle Area", command=show_circle_area).grid(row=5, column=2)

# Create widgets for BMI calculation
tk.Label(root, text="Weight (kg):").grid(row=6, column=0)
weight_entry = tk.Entry(root)
weight_entry.grid(row=6, column=1)
tk.Label(root, text="Height (m):").grid(row=7, column=0)
height_entry = tk.Entry(root)
height_entry.grid(row=7, column=1)
tk.Button(root, text="Calculate BMI", command=show_bmi).grid(row=6, column=2, rowspan=2)

# Create widgets for simple interest calculation
tk.Label(root, text="Principal Amount:").grid(row=8, column=0)
principal_entry = tk.Entry(root)
principal_entry.grid(row=8, column=1)
tk.Label(root, text="Rate (%):").grid(row=9, column=0)
rate_entry = tk.Entry(root)
rate_entry.grid(row=9, column=1)
tk.Label(root, text="Time (years):").grid(row=10, column=0)
time_entry = tk.Entry(root)
time_entry.grid(row=10, column=1)
tk.Button(root, text="Calculate Interest", command=show_simple_interest).grid(row=8, column=2, rowspan=3)

# Create widgets for currency conversion
tk.Label(root, text="Amount to Convert:").grid(row=11, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=11, column=1)
tk.Label(root, text="Conversion Rate:").grid(row=12, column=0)
conversion_rate_entry = tk.Entry(root)
conversion_rate_entry.grid(row=12, column=1)
tk.Button(root, text="Convert Currency", command=show_currency_conversion).grid(row=11, column=2, rowspan=2)

# Button for the guessing game
tk.Button(root, text="Play Guessing Game", command=guess_number_game).grid(row=13, column=0, columnspan=3)

# Start the main loop
root.mainloop()
