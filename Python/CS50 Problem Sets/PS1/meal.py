def main():
    user_input = input("What time is it? (military ##:## or ##:## am/pm) ")
    print(convert(user_input))

def convert(time):
    time = time.strip()
    hourChange = 0

    # hourChange is used to help support 12-hour times and military time conversion

    try:
        x, y = time.split()
        y = y.replace(".", "").lower()
        match y:
            case "am":
                if x.startswith("12"):
                    hourChange = -12
            case "pm":
                if x.startswith("12"):
                    pass
                else:
                    hourChange = 12
    except:
        x = time

    hours, minutes = x.split(":")
    hours = int(hours) + hourChange
    minutes = int(minutes)
    totalMinutes = minutes + (hours * 60)

    if totalMinutes >= (7 * 60) and totalMinutes <= (8 * 60):
        return "breakfast time"
    elif totalMinutes >= (12 * 60) and totalMinutes <= (13 * 60):
        return "lunch time"
    elif totalMinutes >= (18 * 60) and totalMinutes <= (19 * 60):
        return "dinner time"
    else:
        return "It's " + str(hours) + ":" + str(minutes) + " in military time."

    # I added the else condition so that I can see if the program still runs correctly and converts to military time

if __name__ == "__main__":
    main()