def check_plate(input):
    numbersFound = False

    # Check Length
    if len(input) < 2 or len(input) > 6:
        return "INVALID"
    
    # Check Appropriate Characters
    if input.isalnum() == False:
        return "INVALID"
    
    # Check First Two Characters
    if input[0:2].isalpha() == False:
        return "INVALID"
    
    # Check Number Placements
    for each in input:
        if numbersFound == True:
            if each.isdecimal() == False:
                return "INVALID"
        elif numbersFound == False:
            if each.isdecimal() and each == "0":
                return "INVALID"
            elif each.isdecimal():
                numbersFound = True

    return "VALID"

def main():
    user_input = input("Plate: ")
    print(check_plate(str(user_input)))

if __name__ == "__main__":
    main()