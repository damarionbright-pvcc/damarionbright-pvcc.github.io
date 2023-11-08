# Name: Damarion Bright
# Prog Purpose: This program finds the cost of pet vaccines & medications for dogs and cats

# NOTE: Pet medications prescribed by licensed veterinarians are not subject to sales tax in Virginia

# Pet care meds pricing
# -----------------------------
# Canine vaccines:
#     1. Bordatella $30.00
#     2. DAPP $35.00
#     3. Influenza $48.00
#     4. Leptospirosis $21.00
#     5. Lyme Disease $41.00
#     6. Rabies $25.00
#     7. Full vaccine package (includes all vaccines): 15% discount
#
# Canine heartworm preventative chews (price per chew; one chew per month)
# Small dogs, up to 25 lbs: $9.99
# Medium-sized dogs, 26 to 50 lbs: $11.99
# Large dogs: 51 to 100 lbs: $13.99

import datetime

############## Define global variables ############
# Define dog prices
PR_BORD = 30.00
PR_DAPP = 35.00
PR_FLU = 48.00

PR_ALL = 0

PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99

more = True  # Initialize the 'more' variable

############## Define program functions ################
def main():
    global more  # Use the global 'more' variable

    while more:
        get_user_data()

        if pet_type.upper() == "D":
            get_dog_data()
            perform_dog_calculations()
            display_dog_results()
        else:
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()

        askAgain = input("\nWould you like to process another pet (Y/N)?: ")
        if askAgain.upper() == "N":
            more = False
            print('Thank you for trusting Pet Care Meds with your pet vaccines and medications.')

def get_user_data():
    global pet_name, pet_type, pet_weight
    pet_name = input("Pet name: ")  # Keep it as a string
    pet_type = input("Is this pet a dog (D) or cat (C)? ").upper()  # Convert to uppercase
    pet_weight = float(input("Weight of your pet (in pounds): "))  # Use float for weight

################ DOG functions ################

def get_dog_data():
    global pet_vax_type, num_chews
    dog1 = "\n**Dog vaccines: \n\t1. Bordatella \n\t2. DAPP \n\t3. Influenza \n\t4. Leptospirosis"
    dog2 = "\n\t5. Lyme disease \n\t6. Rabies \n\t7. Full vaccine package \n\t8. None"
    dogmenu = dog1 + dog2
    pet_vax = int(input(dogmenu + "\n** Enter the vaccine number: "))

    print("\nMonthly heartworm prevention medication is recommended for all dogs.")
    heart_yesno = input("Would you like to order monthly heartworm medication for " + pet_name + " (Y/N): ")
    if heart_yesno.upper() == "Y":
        num_chews = int(input("How many heartworm chews would you like to order? "))

def perform_dog_calculations():
    print("Dog Calculations")

def display_dog_results():
    print("Display Dogs")

################ Cat functions ################
def get_cat_data():
    print("Cat Data")

def perform_cat_calculations():
    print("Cat Calculations")

def display_cat_results():
    print("Display Cats")

# Start the program by calling the main function
if __name__ == "__main__":
 main()
