import random

def main():
    level = get_level()
    generate_level(level)

def get_level():
    print("Select Your Level (1, 2, of 3)")

    while True:
        try:
            user_input = int(input("Choose Level: ").strip())
            if user_input > 0 and user_input < 4:
                return user_input
            else:
                pass
        except:
            pass

        print("Input error, please input 1, 2, or 3.")

def generate_level(level: int):
    question = 0
    score = 0
    tries = 0
    x = 0
    y = 0
    z = 0

    print("You will have three tries for each question.")
    print("Starting Level " + str(level))

    while question < 10:
        question += 1
        tries = 0

        if level == 1:
            x = random.randint(1, 3) 
            y = random.randint(1, 3)
        elif level == 2:
            x = random.randint(1, 5) 
            y = random.randint(1, 5)
        else:
            x = random.randint(1, 10) 
            y = random.randint(1, 10)

        # Threw some level progression into the assignment

        z = x + y

        while tries < 3:
            tries += 1

            try:
                user_input = int(input(str(x) + " + " + str(y) + " = ").strip())
                if user_input == z:
                    score += 1
                    break
            except:
                pass

            print("EEE: " + str(tries) + "/3")
            if tries == 3:
                print("Correct Answer: " + str(x) + " + " + str(y) + " = " + str(z))
            
    print("Score: " + str(score) + "/10")
    
if __name__ == "__main__":
    main()