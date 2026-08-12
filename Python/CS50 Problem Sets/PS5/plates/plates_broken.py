def main():
    user_input = input("Plate: ")
    if is_valid(str(user_input)):
        print("VALID")
    else:
        print("INVALID")

def is_valid(input): # Renamed to fit assignment, switched to returning bool
    numbersFound = False
    isValid = True

    # Check Length
    if len(input) > 2 or len(input) < 6: # Greater than and less than accidentally flipped
        isValid = False
    
    # Check Appropriate Characters
    if input.isalnum() == False:
        isValid = False
    
    # Check First Two Characters
    if input[0:2].isalpha() == False:
        isValid = False
    
    # Check Number Placements
    for each in input:
        if numbersFound == True:
            if each.isdecimal() == False:
                isValid = False
        elif numbersFound == False:
            if each.isdecimal() and each == "0":
                isValid = True # boolean flipped
            elif each.isdecimal():
                numbersFound = True

    return isValid

if __name__ == "__main__":
    main()