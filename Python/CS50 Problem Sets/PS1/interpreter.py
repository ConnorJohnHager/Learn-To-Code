def answerCheck(x, y, z):
    answer = "null"

    try:
        x = float(x)
        z = float(z)
    except:
        return answer
    
    match y:
        case "+":
            answer = x + z
        case "-":
            answer = x - z
        case "*":
            answer = x * z
        case "/":
            answer = x / z
    
    if answer != "null":
        return float.from_number(answer)
    else:
        return "null"

    # I added this if-statement to inform the user if there was an error 

def main():
    user_input = input("Expression: ")
    x, y, z = user_input.split(" ")
    check = answerCheck(x, y, z)

    if check != "null":
        print(check)
    else:
        print("This doesn't seem like a simple math equation.")

main()