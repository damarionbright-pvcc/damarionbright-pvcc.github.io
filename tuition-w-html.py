#Name: Lewis Fassero & Damarion Bright
#Program Purpose: This program finds the balance of tuition and fees owed by a student.

import datetime

##### define global variables #####

# define tax rate and prices
RATETUITIONIN = 159.61
RATETUITIONOUT = 336.21
RATECAPITALFEE = 23.50
RATEINSTITUTIONFEE = 1.75
RATEACTIVITYFEE = 2.90

# define global variables
inout = 1  # 1 means in state, 2 means out of state
num_credits = 0
scholarshipamt = 0
tuitiontotal = 0
capitaltotal = 0
institutiontotal = 0
activitytotal = 0
subtotal = 0
total = 0

# create output file
outfile = 'tuition.html'

##### define program functions #####

def main():
    open_outfile()
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to calculate tuition and fees for another student? (Y or N): ")
        if yesno.upper() == "N":
            more = False
            print('\n** Open this file in a browser window to see your results: ' + outfile)
            f.write('</body></html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> Piedmont Virginia Community College </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-color: #FBFBFB; background-image: url(wp-tuition.jpg); color: #000000">\n')

def get_user_data():
    global inout, num_credits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE or a 2 for OUT-OF-STATE: "))
    num_credits = int(input("How many credits did you register for?: "))
    scholarshipamt = float(input("Scholarship amount received: "))

def perform_calculations():
    global tuitiontotal, capitaltotal, institutiontotal, activitytotal, subtotal, total
    if inout == 1:
        tuitiontotal = num_credits * RATETUITIONIN
        capitaltotal = 0
    else:
        tuitiontotal = num_credits * RATETUITIONOUT
        capitaltotal = num_credits * RATECAPITALFEE
    
    institutiontotal = num_credits * RATEINSTITUTIONFEE
    activitytotal = num_credits * RATEACTIVITYFEE
    subtotal = tuitiontotal + capitaltotal + institutiontotal + activitytotal
    total = subtotal - scholarshipamt

def display_results():
    global f, inout, num_credits, tuitiontotal, capitaltotal, institutiontotal, activitytotal, subtotal, total
    tr = '<tr><td>'
    endtd = '</td><td>'
    endtr = '</td></tr>\n'

    f.write('\n<table border="3" style="background-color: #004FA8; font-family: arial; margin: auto;">\n')
    f.write('<tr><td colspan="2"><h2>Piedmont Virginia Community College</h2></td></tr>')
    f.write('<tr><td colspan="2">*** PVCC is for YOU ***</td></tr>')

    f.write(tr + 'Tuition' + endtd + str(num_credits) + endtd + format(tuitiontotal, ',.2f') + endtr)
    f.write(tr + 'Capital fee' + endtd + str(num_credits) + endtd + format(capitaltotal, ',.2f') + endtr)
    f.write(tr + 'Institution fee' + endtd + str(num_credits) + endtd + format(institutiontotal, ',.2f') + endtr)
    f.write(tr + 'Activity fee' + endtd + str(num_credits) + endtd + format(activitytotal, ',.2f') + endtr)

    f.write(tr + 'Subtotal' + endtd + endtd + format(subtotal, ',.2f') + endtr)
    f.write(tr + 'Scholarship' + endtd + endtd + format(scholarshipamt, ',.2f') + endtr)
    f.write(tr + 'Amount due' + endtd + endtd + format(total, ',.2f') + endtr)

    f.write('<tr><td colspan="2">Date/Time: ' + str(datetime.datetime.now()) + '</td></tr>')
    f.write('</table>')

##### call on main program to execute #####
if __name__ == "__main__":
    main()
