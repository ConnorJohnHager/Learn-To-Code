from pyfiglet import Figlet
figlet = Figlet()

# Remember to input 'python -m pip install pyfiglet' in your terminal to be able to import

import sys
import random

def select_font():
    list = figlet.getFonts()

    try: 
        if sys.argv[1] != "":
            pass
    except:
        newFont = random.choice(list)
        figlet.setFont(font=newFont)
        return
    
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        try:
            newFont = sys.argv[2]
            if list.__contains__(newFont): # Checking to make sure font exists
                figlet.setFont(font=newFont)
                return
        except:
            pass

    sys.exit("Invalid usage")

def process_input():
    user_input = input("Input: ").strip()
    print("Output:")
    print(figlet.renderText(user_input))

def main():
    select_font()
    process_input()

if __name__ == "__main__":
    main()