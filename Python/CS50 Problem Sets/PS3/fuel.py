import math

# Must have this in your system

def answerCheck(input):
    try:
        x_str,y_str = input.split("/")
        x = int(x_str)
        y = int(y_str)
        if x < 0:
            raise ValueError

        tank = math.floor((x / y) * 100)
        
        if tank > 100:
            raise ValueError
        elif tank == 100:
            return "F"
        elif tank == 0:
            return "E"
        return str(tank) + "%"
    
    except ValueError:
        return ValueError
    except ZeroDivisionError:
        return ZeroDivisionError
    except:
        return "Unknown Error"

    # I added this to tell the user what type of error occurred

def main():
    user_input = input("Fraction: ")
    print(answerCheck(user_input))

if __name__ == "__main__":
    main()