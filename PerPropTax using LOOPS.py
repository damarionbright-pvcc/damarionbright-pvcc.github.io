# Name: Damarion Bright



def calculate_tax(assessed_value, eligible_for_relief):
    # Personal property tax rate
    tax_rate = 4.20 / 100  # 4.20% per year

    # Calculate annual tax amount
    annual_tax_amount = assessed_value * tax_rate

    # Divide tax amount by 2 for six-month bill
    six_month_tax = annual_tax_amount / 2

    # Check if the vehicle is eligible for tax relief
    if eligible_for_relief == 'Y':
        # Calculate relief amount (33% of the six-month tax)
        relief_amount = six_month_tax * 0.33
    else:
        relief_amount = 0

    # Calculate total due for six months
    total_due = six_month_tax - relief_amount

    return six_month_tax, relief_amount, total_due

def print_bill(assessed_value, six_month_tax, relief_amount, total_due):
    print("\nPersonal Property Tax Bill")
    print("-------------------------")
    print("Assessed value of the vehicle: {}".format(format_currency(assessed_value)))
    print("Full annual amount owed: {}".format(format_currency(six_month_tax * 2)))
    print("Relief amount: {}".format(format_currency(relief_amount * 2)))
    print("Total due: {}".format(format_currency(total_due * 2)))
    print("-------------------------")

def format_currency(amount):
    return "${:,.2f}".format(amount)

# Main program loop
while True:
    print("\nCharlottesville Personal Property Tax Calculator")
    assessed_value = float(input("Enter the assessed value of the vehicle: "))
    eligible_for_relief = input("Is the vehicle eligible for tax relief? (Y/N): ").upper()

    six_month_tax, relief_amount, total_due = calculate_tax(assessed_value, eligible_for_relief)

    print_bill(assessed_value, six_month_tax, relief_amount, total_due)

    choice = input("\nCalculate another vehicle tax? (Y/N): ").upper()
    if choice != 'Y':
        break
