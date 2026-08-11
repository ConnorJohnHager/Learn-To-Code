import inflect
p = inflect.engine()

# Remember to input 'python -m pip install inflect' in your terminal to be able to import

def main():
    print("Who would you like to say Adieu to? Hit 'Enter' with no name to complete the list.")

    #Used a blank input instead of EOFError to close out

    names = []

    while True:
        user_input = input("Name: ").strip()
        if user_input != "":
            names.append(user_input)
        else:
            break

    print("Adieu, adieu, to " + p.join(names))

    # See 'Join Words into a List' from https://pypi.org/project/inflect/

if __name__ == "__main__":
    main()