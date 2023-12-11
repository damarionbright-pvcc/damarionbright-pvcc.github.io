#name: Damarion Bright
# Prog Purpose: This program creates a Emerald Beach Hotel & Resort report



import csv
import os

# Room rates dictionary
room_rates = {
    'SR': 195.00,
    'DR': 250.00,
    'SU': 350.00
}

# Tax rates
sales_tax_rate = 6.5 / 100
occupancy_tax_rate = 11.25 / 100

# File path for the CSV file
file_path = 'emeraldd.csv'  # Update this path if necessary

if os.path.exists(file_path):
    print(f"File '{file_path}' exists.")
    # Initialize data as an empty list
    data = []

    # Read data from CSV file
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            data.append(row)

    # Process data and perform calculations
    grand_total = 0
    for guest in data:
        last_name, first_name, room_type, num_nights = guest

        # Calculate subtotal based on room type and number of nights
        subtotal = int(num_nights) * room_rates.get(room_type, 0)

        # Calculate taxes
        sales_tax = subtotal * sales_tax_rate
        occupancy_tax = subtotal * occupancy_tax_rate

        # Calculate total amount
        total = subtotal + sales_tax + occupancy_tax

        # Append amounts to the guest list
        guest.extend([f'${subtotal:.2f}', f'${sales_tax:.2f}', f'${occupancy_tax:.2f}', f'${total:.2f}'])

        # Update grand total
        grand_total += total

    # Append grand total to the last row of the data
    data.append(['', '', '', '', '', '', '', '', f'Grand Total: ${grand_total:.2f}'])

    # Generate HTML report
    with open('hotelsalesrep.html', 'w') as html_file:
        html_file.write('''
        <html>
        <head>
            <title>Emerald Beach Hotel & Resort - Sales Report</title>
            <style>
                body {
                    background-image: url('meto.jpg'); /* Path to your background image */
                    background-color: #FBFBFB;
                    font-family: Arial, sans-serif;
                    color: #E600FF;
                }
                table {
                    border-collapse: collapse;
                    width: 100%;
                    margin: 20px auto;
                }
                th, td {
                    border: 1px solid #dddddd;
                    text-align: center;
                    padding: 8px;
                }
                th {
                    background-color: #f2f2f2;
                }
                caption {
                    text-align: center;
                    font-size: 24px;
                    margin-bottom: 10px;
                }
            </style>
        </head>
        <body>
        <caption>Emerald Beach Hotel & Resort - Sales Report</caption>
        <table>
            <tr>
                <th>Last Name</th>
                <th>First Name</th>
                <th>Room Type</th>
                <th>Num Nights</th>
                <th>Subtotal</th>
                <th>Sales Tax</th>
                <th>Occ. Tax</th>
                <th>Total</th>
            </tr>
        ''')

        for row in data:
            html_file.write('<tr>')
            for col in row:
                html_file.write(f'<td>{col}</td>')
            html_file.write('</tr>')

        html_file.write('''
        </table>
        </body>
        </html>
        ''')
else:
    print(f"File '{file_path}' does not exist.")
