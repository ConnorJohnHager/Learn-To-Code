import emoji

# Remember to input 'python -m pip install emoji' in your terminal to be able to import

def main():

    print("Input an emoji's code in the following format - :insert_words: ")
    user_input = input("Input: ").strip().lower()

    output = emoji.emojize(user_input, language="alias")

    if output == user_input:
        output = emoji.emojize(user_input)

    if output == user_input:
        print("Cannot find an emoji for " + output)
    else:
        print("Output: " + output)

    # Tests both alias and non-alias for emoji, then informs the user if one can't be located.
    
if __name__ == "__main__":
    main()