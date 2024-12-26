def main():
    # Entry of employee details
    first_name = input("Enter employee's first name: ")
    last_name = input("Enter employee's last name: ")
    employee_id = input("Enter employee ID: ")
    dependents = int(input("Enter number of dependents: "))
    hours_worked = float(input("Enter hours worked: "))
    hourly_rate = float(input("Enter hourly rate: "))

    # Calculate gross pay
    gross_pay = calculate_gross_pay(hours_worked, hourly_rate)

    # Calculate deductions
    dependent_deduction = calculate_dependent_deduction(dependents)
    state_tax = calculate_state_tax(gross_pay)
    federal_tax = calculate_federal_tax(gross_pay)

    # Calculate pre-tax and post-tax amounts
    pre_tax_amount = gross_pay - dependent_deduction
    post_tax_amount = pre_tax_amount - state_tax - federal_tax

    # Display results
    display_results(first_name, last_name, employee_id, gross_pay, dependent_deduction, state_tax, federal_tax, pre_tax_amount, post_tax_amount)

    # End program
    end_program()

# Function to calculate gross pay
def calculate_gross_pay(hours_worked, hourly_rate):
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * hourly_rate * 1.5
        regular_pay = 40 * hourly_rate
        return regular_pay + overtime_pay
    else:
        return hours_worked * hourly_rate

# Function to calculate dependent deduction
def calculate_dependent_deduction(dependents):
    return dependents * 25

# Function to calculate state tax
def calculate_state_tax(gross_pay):
    return gross_pay * 0.056

# Function to calculate federal tax
def calculate_federal_tax(gross_pay):
    return gross_pay * 0.079

# Function to display results
def display_results(first_name, last_name, employee_id, gross_pay, dependent_deduction, state_tax, federal_tax, pre_tax_amount, post_tax_amount):
    print(f"Employee: {first_name} {last_name} (ID: {employee_id})")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print(f"Dependent Deduction: ${dependent_deduction:.2f}")
    print(f"State Tax: ${state_tax:.2f}")
    print(f"Federal Tax: ${federal_tax:.2f}")
    print(f"Pre-Tax Amount: ${pre_tax_amount:.2f}")
    print(f"Post-Tax Amount: ${post_tax_amount:.2f}")

# Function to end the program
def end_program():
    print("Thank you for using the payroll program. Goodbye!")

# Start the program
main()
