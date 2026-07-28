def slow_playback(text):
    text = text.replace(" ", "...")
    return text

def main():
    user_input = input()
    print(slow_playback(user_input))

main()