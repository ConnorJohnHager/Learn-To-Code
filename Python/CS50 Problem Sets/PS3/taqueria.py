def correct_capitalization(input):
    input = input.strip().lower()
    newValue = ""
    cap = True

    for letter in input:
        if cap:
            letter = letter.upper()
            cap = False
        elif letter == " ":
            cap = True
        newValue = str(newValue + letter)

    return newValue

def order_item():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    while True:
        try:
            request = correct_capitalization(input("Item: "))
        
            if request == "":
                return 0
            elif request in menu:
                return menu[request]
            else:
                print("We can't locate this item. Please try again.")
        except EOFError:
            return 0

        # EOFError is triggered differently between Mac and Windows
        # I added another condition to trigger finalizing the list

def main():
    total = 0
    request = 1

    print("Welcome to our restaurant! Please place your order:")

    while request != 0:
        request = order_item()
        if request == 0:
            break
        total += request
        print(f"Total: ${total:.2f}")
        print("When you are done ordering, hit Enter with no item requested.")
    
    print("Thank you for eating with us today!")
    
if __name__ == "__main__":
    main()