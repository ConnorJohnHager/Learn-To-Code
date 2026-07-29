def convert_to_snake_case(input):
    newValue = ""
    for letter in input:
        if letter.isupper():
            newValue = str(newValue + "_" + letter.lower())
        else:
            newValue = str(newValue + letter)
    return newValue

def main():
    user_input = input("camelCase: ")
    print("snake_case: " + convert_to_snake_case(str(user_input)))

if __name__ == "__main__":
    main()