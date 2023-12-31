"""A morse code encoder/decoder"""
import pyfiglet

# Gay absoultely gay
# This requires no explaination
# Actually gay
# legit gay
pyfiglet.figlet_format('=== MORSE CODE TRANSLATOR ===')
print('''
DISCLAIMER: Only valid morse code letter will be shown in the translation
For translation of text to morse code, please choose 1
For translation of morse code to text, please choose 2
''')

# Status to exit while loo[]
EXIT_STATUS = False

# Ignore this
class GoToHell(Exception):
    """Exception"""

# Lists
MORSE = ['/', '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
         '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-',
         '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--',
         '....-', '.....', '-....', '--...', '---..', '----.', '.-...', '.---.', '.--.-.',
         '-.--.-', '-.--.', '---...', '--..--', '-...-', '-.-.--', '.-.-.-', '-....-',
         '------..-.-----', '.-.-.', '-....-', '..--..', '-..-.']
CHARACTERS = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', 
              '1', '2', '3', '4', '5', '6', '7', '8', '9', '&', "'", '@', ')', '(',
              ':', ',', '=', '!', '.', '-', '%', '+', '"', '?', '/']


while EXIT_STATUS is False:
    while True:

        # Gets user choice - no explaination needed
        try:
            choice = int(input("Enter 1 or 2: "))
            if choice == 1 or choice == 2:
                break
            else:
                print("Invalid input. Please enter a number (1 or 2).")

        except ValueError:
            print("Invalid input. Please enter a number (1 or 2).")

    # Choice to translate text to morse
    if choice == 1:
        MESSAGE = str(input("Please input or paste your text here: "))

        MORSE_MESSAGE = ''

        # find the character in the list - assuming its in there
        for char in MESSAGE:
            MORSE_MESSAGE += MORSE[CHARACTERS.index(char.lower())]
        print(f"Morse: {MORSE_MESSAGE}")

    # Choice to translate morse to text
    elif choice == 2:
        MORSE_MESSAGE = str(input("Please input or paste your morse here:"))

        # Translate morse to text - assuming khanh did the job
        MESSAGE = ''
        for char in MORSE_MESSAGE:
            MESSAGE += CHARACTERS[MORSE.index(char.lower())]
        print(f"Text: {MESSAGE}")

    else:
        raise GoToHell

    while True:
        # Self Explainatory
        EXIT_STATUS = str(input("Do you want to continue? (y/n) "))
        if EXIT_STATUS.lower() == 'y':
            EXIT_STATUS = False
            break
        elif EXIT_STATUS.lower() == 'n':
            EXIT_STATUS = True
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
