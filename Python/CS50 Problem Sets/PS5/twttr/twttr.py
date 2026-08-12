def main():
    user_input = input("Input: ")
    print("Output: " + shorten(str(user_input)))

def shorten(input): # Renamed to fit assignment
    newValue = ""
    vowels = ["a", "e", "i", "o", "u"]

    for letter in input:
        if letter.lower() in vowels:
            pass
        else:
            newValue = str(newValue + letter)
    return newValue

if __name__ == "__main__":
    main()