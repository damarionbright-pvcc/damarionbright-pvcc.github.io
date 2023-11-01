#Name: Lewis Fassero & Damarion Bright
#Program Purpose: This program finds the balance of tuition and fees owed by a student.

import datetime

##### define global variables #####
# define tax rate and prices
RATETUITIONIN=159.61
RATETUITIONOUT=336.21
RATECAPITALFEE=23.50
RATEINSTITUTIONFEE=1.75
RATEACTIVITYFEE=2.90

# define global variables
inout=1 #1 means in state, 2 means out of state
num_credits=0
scholarshipamt=0
tuitiontotal=0
capitaltotal=0
institutiontotal=0
activitytotal=0
subtotal=0
total=0

##### define program functions ####

def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to calculate tuition and fees for another student? (Y or N): ")
        if yesno.upper() == "N":
            more = False

def get_user_data():
    global inout, num_credits, scholarshipamt
    inout=int(input("Enter a 1 for IN-STATE or a 2 for OUT-OF-STATE: "))
    num_credits=int(input("How many credits did you register for?: "))
    scholarshipamt=float(input("Scholarship amount received: "))

def perform_calculations():
    global tuitiontotal, capitaltotal, institutiontotal, activitytotal, subtotal, total
    if inout==1:
        tuitiontotal=num_credits*RATETUITIONIN
    else: tuitiontotal=num_credits*RATETUITIONOUT
    
    if inout==1:
        capitaltotal=0
    else: capitaltotal=num_credits*RATECAPITALFEE

    institutiontotal=num_credits*RATEINSTITUTIONFEE
    activitytotal=num_credits*RATEACTIVITYFEE
    subtotal=tuitiontotal+capitaltotal+institutiontotal+activitytotal
    total=subtotal-scholarshipamt

def display_results():
    moneyformat='8,.2f'
    qtyformat='2'
    print('-----------------------------------------')
    print('** Piedmont Virginia Community College **')
    print('*************PVCC is for YOU*************')
    print('-----------------------------------------')
    print(format(num_credits, qtyformat) + '  Tuition                    $ ' + format(tuitiontotal, moneyformat))
    print(format(num_credits, qtyformat) + '  Capital fee                $ ' + format(capitaltotal, moneyformat))
    print(format(num_credits, qtyformat) + '  Institution fee            $ ' + format(institutiontotal, moneyformat))
    print(format(num_credits, qtyformat) + '  Activity fee               $ ' + format(activitytotal, moneyformat))
    print('                             ')
    print('    Subtotal:                  $ ' + format(subtotal, moneyformat))
    print('    Scholarships:              $ ' + format(scholarshipamt, moneyformat))
    print('    Amount due:                $ ' + format(total, moneyformat))
    print('-----------------------------------------')
    print(str(datetime.datetime.now()))

##### call on main program to execute #####

main()
