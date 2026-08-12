import math

# Refactored to match the assignment

def main():
    user_input = input("Fraction: ")
    print(gauge(convert((user_input))))

def convert(fraction): # Return Int
    try:
        x_str,y_str = fraction.split("/")
        x = int(x_str)
        y = int(y_str)
        if x < 0 or y < 0:
            raise ValueError
    
        tank = math.floor((x / y) * 100)

        return tank

    except ValueError:
        return ValueError
    except ZeroDivisionError:
        return ZeroDivisionError
    except:
        return "Unknown Error"

def gauge(percentage): # Return String
    if percentage > 100:
        return ValueError
    elif percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    
    return str(percentage) + "%"

if __name__ == "__main__":
    main()