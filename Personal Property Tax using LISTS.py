# Name Damarion Bright
# program:this program uses lists to find the personal property tax for vehicles in charlottesville
#         and produces a report which displays all data and the total tax due
#
# personal property tax in charlottesville:
#     --  $4.20 per $100 of vehicle value (4.20% year)
#     -- paid every six months
# personal property tax relief (PPTR):
#   --  Eligibility: owned or leased vehicles which are predominately used for non-business purposes & have passenger license plates
#   -- tax relief for qualified vehicles is 33%

import datetime

# Define tax rates
PPT_RATE = 0.042
RELIEF_RATE = 0.33

# Create list data
vehicle = [
    "2019 Volvo",
    "2018 Toyota",
    "2022 Kia",
    "2020 Ford",
    "2023 Honda",
    "2019 Lexus"
]

vehicle_value = [13000, 10200, 170000, 21000, 28000, 16700]
pptr_eligible = ["Y", "Y", "N", "Y", "N", "Y"]

owner_name = [
    "Brand, Debra",
    "Smith, Carter",
    "Johnson, Bradley",
    "Garcia, Jennifer",
    "Henderson, Leticia",
    "White, Danielle"
]

ppt_owed = []
num_vehicles = len(vehicle)
total = 0  # Removed tax_due variable as it's calculated in the loop

# Define program functions

def main():
    perform_calculations()
    display_results()

def perform_calculations():
    global total

    for i in range(num_vehicles):
        tax_due = (vehicle_value[i] * PPT_RATE / 2)

        if pptr_eligible[i].upper() == "Y":
            tax_due *= (1 - RELIEF_RATE)

        ppt_owed.append(tax_due)
        total += tax_due

def display_results():
    line = '--------------------------------'
    tab = "\t"
    print(line)
    print('******************** PERSONAL PROPERTY TAX REPORT ************************')
    print('-------------------- Charlottesville, Virginia --------------------')
    print("\n\t\tRUN DATE/TIME: " + str(datetime.datetime.now()))
    print("\nNAME" + tab + tab + tab + "VEHICLE" + tab + tab + "VALUE" + tab + tab + "RELIEF" + tab + "TAX DUE")

    for i in range(num_vehicles):
        data_line1 = owner_name[i] + tab + vehicle[i] + tab + "${:,.2f}".format(vehicle_value[i]) + tab
        data_line2 = pptr_eligible[i] + tab + tab + "${:,.2f}".format(ppt_owed[i])
        print(data_line1 + data_line2)

    print(line)
    print("******************************************** TOTAL TAX DUE:" + tab + "${:,.2f}".format(total))

main()
