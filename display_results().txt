# Name: Damarion Bright
# Prog Purpose: This program creates a payroll report

import datetime

# Lists of data
emp = [
    "Smith, James     ",
    "Johnson, Patricia",
    "Williams, John   ",
    "Brown, Michael   ",
    "Jones, Elizabeth ",
    "Garcia, Brian    ",
    "Miller, Deborah  ",
    "Davis, Timothy   ",
    "Rodriguez, Ronald",
    "Martinez, Karen  ",
    "Hernandez, Lisa  ",
    "Lopez, Nancy     ",
    "Gonzales, Betty  ",
    "Wilson, Sandra   ",
    "Anderson, Margie ",
    "Thomas, Daniel   ",
    "Taylor, Steven   ",
    "Moore, Andrew    ",
    "Jackson, Donna   ",
    "Martin, Yolanda  ",
    "Lee, Carolina    ",
    "Perez, Kevin     ",
    "Thompson, Brian  ",
    "White, Deborah   ",]
job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
       "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M"]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_emps = len(emp)

# New lists for calculated amounts
gross_pay = []
fed_tax = []
state_tax = []
soc_sec = []
medicare = []
net_pay = []

total_gross = 0
total_net = 0

# Tuples of constants
# Added a placeholder rate for the fourth job type
PAY_RATE = (16.50, 15.75, 15.75, 19.50)
DED_RATE = (0.012, 0.03, 0.062, 0.0145, 0.04)

def main():
    perform_calculations()
    display_results()

def perform_calculations():
    global total_gross, total_net, gross_pay, fed_tax, state_tax, soc_sec, medicare, net_pay

    for i in range(num_emps):
        # calculate gross pay based on job type
        if job[i] == "C":
            pay = hours[i] * PAY_RATE[0]
        elif job[i] == "S":
            pay = hours[i] * PAY_RATE[1]
        elif job[i] == "J":
            pay = hours[i] * PAY_RATE[2]
        else:
            pay = hours[i] * PAY_RATE[3]

        # calculate deductions
        fed = pay * DED_RATE[0]
        state = pay * DED_RATE[1]
        # Calculate other deductions and NET PAY here:
        soc = pay * DED_RATE[2]
        medic = pay * DED_RATE[3]

        net = pay - (fed + state + soc + medic)

        # add to totals
        total_gross += pay
        total_net += net

        # append amounts to lists
        gross_pay.append(pay)
        fed_tax.append(fed)
        state_tax.append(state)
        soc_sec.append(soc)
        medicare.append(medic)
        net_pay.append(net)

def display_results():
    out_file = "payroll_report.txt"  # File name for the output report
    currency = '${:,.2f}'
    line = '\n--------------------------------'
    tab = "\t"

    with open(out_file, 'w') as f:  # Open the file for writing
        f.write(line)
        f.write('\n******************** FRESH FOODS MARKET ************************')
        f.write('\n-------------------- WEEKLY PAYROLL REPORT --------------------')
        f.write('\n' + str(datetime.datetime.now()))
        f.write(line)
        titles1 = "Emp  Name" + tab + "Gross" + tab
        titles2 = "Fed Inc Tax" + tab + "State Inc Tax" + tab + "Soc Sec" + tab + "Medicare" + tab + "Net"
        f.write(titles1 + titles2)

        for i in range(num_emps):
            data1 = "\n" + emp[i] + tab + currency.format(gross_pay[i]) + tab  
            data2 = tab.join([currency.format(val) for val in [fed_tax[i], state_tax[i], soc_sec[i], medicare[i], net_pay[i]]])
            f.write(data1 + data2)

            print(line)
            print(data1 + data2)

        f.write(line)
        f.write("\n******************** TOTAL GROSS: " + currency.format(total_gross))
        f.write("\n******************** TOTAL NET :  " + currency.format(total_net))
        f.write(line)

    print("Open " + out_file + " to view your report")

# Call the main function to execute the program
main()
