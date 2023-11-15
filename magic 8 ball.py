# Name: Damarion Bright
# prog purpose: this magcic 8-ball code uses a python tuple since the
# user does not have the abillity to change the 8-ball answers.
# however, the program could have used a python list instead of a tuple.
# NOTE: Tuples use parenthese; listsnuse square braces.

import random

answers_8_ball = (
    "I see it, yes", "Ask again later", "Better not tell now", "Cannot predict now",
    "Concentrate and ask again", "Don't count on it", "It is certain", "It is decidedly so",
    "Most likely", "My reply is no", "My sources say no", "Outlook good", "Outlook not so good",
    "Reply hazy, try again", "Signs point to yes", "Very doubtful", "Without a doubt", "Yes",
    "Yes definitely", "You may rely on it"
)


def main():
    print("I am the magic-8 ball and can answer any YES or NO question!")

    another_question = True
    while another_question:
        answer = random.choice(answers_8_ball)

        print("\nShake the magic-8 ball")
        print("...and now...")
        question = input("\nWhat is your YES or NO question? ")
        print("The magic-8 ball says: " + answer)

        ask_again = input("\nWould you like to ask me another question (Y or N)?: ")
        if ask_again.upper() == "N":
            another_question = False
            print('\nCome back again when you have other important questions.')
            print("...magic-8 ball out.")


main()  # Call the main function to start the program
