# -------------------------------------------------------------
# Steven Payroll Calculator
# This program calculates:
# - Gross Pay
# - Overtime Pay
# - Payroll Deductions
# - Net Pay
# - Annual Gross Salary
# - Annual Net Salary
# -------------------------------------------------------------

# Function to calculate gross pay including overtime
def calculate_pay(hours_worked, pay_per_hour):

    # Check if employee worked overtime
    if hours_worked > 40:

        # Calculate overtime hours
        overtime = hours_worked - 40

        # Calculate gross pay with overtime pay rate (1.5x)
        gross_pay = (pay_per_hour * 40) + (pay_per_hour * overtime * 1.5)

    else:
        # Regular pay calculation
        gross_pay = pay_per_hour * hours_worked

    return gross_pay


# Function to calculate total payroll deductions
def deductions(gross_pay):

    # Federal tax deduction
    federal = gross_pay * 0.12

    # Minnesota state tax deduction
    state = gross_pay * 0.0535

    # Social Security deduction
    social_security = gross_pay * 0.062

    # Medicare deduction
    medicare = gross_pay * 0.0145

    # Total deductions calculation
    total_deductions = federal + state + social_security + medicare

    return total_deductions


# Function to calculate take-home pay after deductions
def after_tax(gross_pay, total_deductions):

    # Net pay calculation
    net_pay = gross_pay - total_deductions

    return net_pay


# Function to calculate annual gross salary
def gross_salary(gross_pay):

    # Weekly gross pay multiplied by 52 weeks
    pre_tax_salary = gross_pay * 52

    return pre_tax_salary


# Function to calculate annual net salary
def net_salary(net_pay):

    # Weekly net pay multiplied by 52 weeks
    after_tax_salary = net_pay * 52

    return after_tax_salary


# -------------------------------------------------------------
# Main Program
# -------------------------------------------------------------

print("----- Welcome to Steven Pay Calculator -----\n")

# Ask user for hours worked
hours_worked = float(input("Please enter the total of hours worked: "))

# Ask user for hourly pay
pay_per_hour = float(input("Please enter your current pay per hour: $"))

print("\n")

# Calculate gross pay
untax = calculate_pay(hours_worked, pay_per_hour)

# Calculate payroll deductions
deductions_taken = deductions(untax)

# Calculate net pay
taxed = after_tax(untax, deductions_taken)

# Calculate annual gross salary
pre_tax_salary = gross_salary(untax)

# Calculate annual net salary
after_tax_salary = net_salary(taxed)

# Display payroll information
print(f"Gross Pay: ${untax:.2f}")

print(f"Total Deductions: ${deductions_taken:.2f}")

print(f"Net Pay: ${taxed:.2f}\n")

print(f"Annual Gross Pay: ${pre_tax_salary:.2f}")

print(f"Annual Net Pay: ${after_tax_salary:.2f}")

print("\n")

# Ask user if they want another calculation
print("Do you want to do another calculation?")
answer = input("Enter 1 for YES. Enter 2 for NO: ")


# Loop program while user enters 1
while(answer == "1"):

    print("\n")
    print("------------------------------------------")

    # Ask user for hours worked
    hours_worked = float(input("Please enter the total of hours worked: "))

    # Ask user for hourly pay
    pay_per_hour = float(input("Please enter your current pay per hour: $"))

    print("\n")

    # Calculate payroll information
    untax = calculate_pay(hours_worked, pay_per_hour)

    deductions_taken = deductions(untax)

    taxed = after_tax(untax, deductions_taken)

    pre_tax_salary = gross_salary(untax)

    after_tax_salary = net_salary(taxed)

    # Display payroll information
    print(f"Gross Pay: ${untax:.2f}")

    print(f"Total Deductions: ${deductions_taken:.2f}")

    print(f"Net Pay: ${taxed:.2f}\n")

    print(f"Annual Gross Pay: ${pre_tax_salary:.2f}")

    print(f"Annual Net Pay: ${after_tax_salary:.2f}")

    # Ask user if they want another calculation
    print("Do you want to do another calculation?")
    answer = input("Enter 1 for YES. Enter 2 for NO: ")

print("\n")
print("Thank You! Goodbye :D")