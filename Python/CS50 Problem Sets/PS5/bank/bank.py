def main():
    user_input = input()
    print("$" + str(value(user_input)))

def value(text): # Renamed to fit assignment, switched to returning int
    text = text.lower().strip()
    
    if text.startswith("hello"):
        return 0
    elif text.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()