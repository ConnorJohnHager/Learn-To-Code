def answerCheck(text):
    text = text.replace("-", "")
    text = text.lower().strip()
    
    if text == "42" or text == "fortytwo":
        return "Yes"
    return "No"

    # Examples of different inputs that should return "Yes": 
    ## 42, fortytwo, Forty Two, forty-two, FORTY TWO, 4-2, FoRtYtWo

def main():
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    print(answerCheck(user_input))

main()