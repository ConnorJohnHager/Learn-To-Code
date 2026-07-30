def select_date_input():
    while True:
        print("Please select your preferred date structure for inputs:")
        print("1 for Month-Day-Year.")
        print("2 for Day-Month-Year.")

        # Set up a process to allow both input types

        try:
            user_input = input().strip()
            if user_input == "1" or user_input == "2":
                return int(user_input)
            else:
                pass
        except:
            pass

        print("Please try again.")

def convert_date_input(type):
    months = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december"
    ]

    # Lowercased to make easier for comparing with input values

    first = ""
    second = ""
    third = ""

    dayNumber = 0
    monthNumber = 0
    yearNumber = 0

    while True:
        print("Input a date for conversion to Year-Month-Day.")
        increment = 0

        try:
            date = input("Date: ").strip().lower()
            date = date.replace("/", " ")
            date = date.replace("-", " ")
            date = date.replace(".", " ")
            date = date.replace(",", "")
            first, second, third = date.split(" ")
            yearNumber = int(third)
            
            if type == 1:
                dayNumber = int(second)
                if len(first) >= 3:
                    for each in months:
                        increment += 1
                        if each[:3] == first[:3]:
                            monthNumber = increment
                else:
                    monthNumber = int(first)
            else:
                dayNumber = int(first)
                if len(second) >= 3:
                    for each in months:
                        increment += 1
                        if each[:3] == second[:3]:
                            monthNumber = increment
                else:
                    monthNumber = int(second)

            if monthNumber > 12 or dayNumber > 31:
                pass
            else:
                print(f"{yearNumber:04}-{monthNumber:02}-{dayNumber:02}") 
                return
        except:
            pass

        print("Please try again.")

def main():
    dateType = select_date_input()
    convert_date_input(dateType)
    
if __name__ == "__main__":
    main()