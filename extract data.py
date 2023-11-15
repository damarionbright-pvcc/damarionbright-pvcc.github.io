#Name Damarion Bright
# program purpose: Extract data from the date & time
# the three lines below help to find the string positions
#00000000001111111111222222
#01234567890123456789012345
#2023-11-08 19:51:43.993231

import datetime

def main():
    today = str(datetime.datetime.now())

    year = today[0:4]
    month = today[5:7]
    day = today[8:10]
    day_time = today[0:16]

    print("full date/time: " + today)
    print("\tyear:        " + year)
    print("\tmonth:       " + month)
    print("\tday:         " + day)
    print("\tday & time:  " + day_time)

    monthname = ""
    if month == "01":
        monthname = "January"
    elif month == "02":
        monthname = "February"
    elif month == "03":
        monthname = "March"
    elif month == "04":
        monthname = "April"
    elif month == "05":
        monthname = "May"
    elif month == "06":
        monthname = "June"
    elif month == "07":
        monthname = "July"
    elif month == "08":
        monthname = "August"
    elif month == "09":
        monthname = "September"
    elif month == "10":
        monthname = "October"
    elif month == "11":
        monthname = "November"
    else:
        monthname = "December"

    print("\t" + monthname + " " + day + ", " + year)

main()
