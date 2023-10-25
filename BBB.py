# Name: Daniel Aguilar and Damarion Bright
# Prog Purpose: This program display a customer receipt for Branch Barbecue Buffet.
#   Price for adults: $19.95
#   Price for children: $11.95
#   Service fee rate: 10%
#   Sales tax rate: 6.2%

import datetime

##############  define global variables  ############
# define tax rate and prices
SALES_TAX_RATE = .062
PR_ADULTS = 19.95
PR_CHILDREN = 11.95
SERVICE_FEE_RATE = .10

# define global variables
num_adults = 0
adults_cost = 0
num_children = 0
children_cost = 0
service_fee = 0
sales_tax = 0
subtotal = 0
total = 0

############## define program functions ################
def main():

    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nwould you like to order again (Y or N)?: ")
        if askAgain.upper()== "N" or askAgain.upper()== "NO":
            more = False
            print("Thank you for order. Enjoy your meal!")   

def get_user_data():
    global num_adults, num_children
    num_adults = int(input("Number of adults: "))
    num_children = int(input("Number of children: "))

def perform_calculations():
    global subtotal, service_fee, sales_tax, total, adults_cost, children_cost
    adults_cost = num_adults * PR_ADULTS
    children_cost = num_children * PR_CHILDREN
    subtotal = adults_cost + children_cost
    service_fee = subtotal * SERVICE_FEE_RATE
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax + service_fee
    
def display_results():
    
    moneyformat = '8,.2f'
    line = '------------------------------'
    print(line)
    print('**** BRANCH BARBECUE BUFFET ****')
    print('--- Your neighborhood branch ---')
    print(line)
    print('Adults       $ ' + format(adults_cost, moneyformat))
    print('Children     $ ' + format(children_cost, moneyformat))
    print(line)
    print('Subtotal     $ ' + format(subtotal, moneyformat))
    print('Service Fee  $ ' + format(service_fee, moneyformat))
    print('Sales Tax    $ ' + format(sales_tax, moneyformat))
    print('Total        $ ' + format(total, moneyformat))
    print()
    print(str(datetime.datetime.now()))

########## call on main program to execute ############
main()
    
