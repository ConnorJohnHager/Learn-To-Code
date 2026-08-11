import random

def select_level():
    while True:
        try:
            user_input = int(input("Choose Level: ").strip())
            if user_input > 0:
                return user_input
            else:
                pass
        except:
            pass

        print("Input error, please provide a number greater than 0.")

def game_process(level: int):
    value = random.randint(1, level)
    print("Guess a number between 1 and " + str(level) + ".")

    while True:
        try:
            user_input = int(input("Guess: ").strip())
            if user_input > value:
                print("Too large!")
            elif user_input < value and user_input > 0:
                print ("Too small!")
            elif user_input == value:
                break
            else:
                print("Input error, please provide a number greater than 0.")
        except:
            print("Input error, please provide a number greater than 0.")

    print("Just right!")

def main():
    level = select_level()
    game_process(level)
    
if __name__ == "__main__":
    main()