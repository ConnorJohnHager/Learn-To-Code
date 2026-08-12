def main():
    user_input = input()
    print("$" + str(value(user_input)))

def value(text): # Renamed to fit assignment, switched to returning int
    text = text.lower().strip()
    
    if text.startswith("hello"): # Values swapped between first condition and else
        return 100
    elif text.startswith("h"):
        return 20
    else:
        return 0

if __name__ == "__main__":
    main()