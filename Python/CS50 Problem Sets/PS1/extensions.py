def answerCheck(text):
    text = text.lower().strip()

    images = [".gif", ".jpg", ".jpeg", ".png"]
    apps = [".pdf", ".zip"]

    # While I used two arrays, you could use a dictionary instead with some code tweaks

    for each in images:
        if text.endswith(each):
            if each == ".jpg":
                return "image/jpeg"
            return createFileType("image/", each)
    
    for each in apps:
        if text.endswith(each):
            return createFileType("application/", each)
    
    if text.endswith(".txt"):
        return "text/plain"
    else:
        return "application/octet-stream"

def createFileType(type: str, file: str):
    value = type + file
    value = value.replace(".", "")
    return value

def main():
    user_input = input()
    print(answerCheck(user_input))

main()