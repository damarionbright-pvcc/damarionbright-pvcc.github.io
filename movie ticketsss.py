# Name:Damarion Bright
# Prog Purpose: This program finds the cost of movie tickets.
#   Price for ticket: $10.99
#   Price for drink : $4.99
#   price for popcorn: 8.99
#   Sales tax rate: 5.5%

import datetime

##############  define global variables  ############
# define tax rate and prices
SALES_TAX_RATE = .055
PR_TICKET = 10.99
PR_POPCORN = 8.99
PR_DRINK = 4.99

# define global variables
num_ticket = 0
ticket_cost = 0
num_drink = 0
drink_cost = 0
num_popcorn = 0
popcorn_cost = 0
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
    global num_ticket, num_popcorn , num_drink
    num_ticket = int(input("Number of ticket: "))
    num_popcorn = int(input("Number of popcorn: "))
    num_drink = int(input("Number of drink: "))
def perform_calculations():
    global subtotal, sales_tax, total, ticket_cost , popcorn_cost , drink_cost
    ticket_cost = num_ticket * PR_TICKET
    popcorn_cost = num_popcorn * PR_POPCORN
    drink_cost = num_drink * PR_DRINK
    subtotal = ticket_cost + popcorn_cost + drink_cost
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax 
    
def display_results():
    
    moneyformat = '8,.2f'
    line = '------------------------------'
    print(line)
    print('**** CINEMA HOUSE MOVIES ****')
    print('--- Your neighborhood MOVIE HOUSE ---')
    print(line)
    print('ticket       $ ' + format(ticket_cost, moneyformat))
    print('drink        $ ' + format(drink_cost, moneyformat))
    print(line)
    print('Subtotal     $ ' + format(subtotal, moneyformat))
    print('popcorn      $ ' + format(popcorn_cost, moneyformat))
    print('Sales Tax    $ ' + format(sales_tax, moneyformat))
    print('Total        $ ' + format(total, moneyformat))
    print()
    print(str(datetime.datetime.now()))

########## call on main program to execute ############
main()
    
