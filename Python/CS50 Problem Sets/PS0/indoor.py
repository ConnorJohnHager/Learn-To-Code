def indoor_voice(text):
    text = text.lower()
    return text

def main():
    user_input = input()
    print(indoor_voice(user_input))

main()