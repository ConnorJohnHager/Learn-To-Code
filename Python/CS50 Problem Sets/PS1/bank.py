def answerCheck(text):
    text = text.lower().strip()
    
    if text.startswith("hello"):
        return "$0"
    elif text.startswith("h"):
        return "$20"
    else:
        return "$100"

def main():
    user_input = input()
    print(answerCheck(user_input))

main()