def remove_vowels(input):
    newValue = ""
    vowels = ["a", "e", "i", "o", "u"]

    for letter in input:
        if letter.lower() not in vowels:
            newValue = str(newValue + letter)

    return newValue

def main():
    user_input = input("Input: ")
    print("Output: " + remove_vowels(str(user_input)))

if __name__ == "__main__":
    main()