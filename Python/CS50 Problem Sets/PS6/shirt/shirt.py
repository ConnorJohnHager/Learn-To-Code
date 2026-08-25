import sys
from PIL import Image, ImageOps

# Remember to input 'python -m pip install Pillow' in your terminal to be able to import

def main():
    check_argv()
    process_photo()

def check_argv():
    argv = len(sys.argv) - 1
    if argv < 2:
        sys.exit("Too few command-line arguments")
    elif argv > 2:
        sys.exit("Too many command-line arguments")

    pictureTypes = [".jpg", ".jpeg", ".png"]
    fileName = sys.argv[1].lower()
    newFileName = sys.argv[2].lower()
    doesItPass1 = False
    doesItPass2 = False

    for each in pictureTypes:
        if fileName.endswith(each):
            doesItPass1 = True

        if newFileName.endswith(each):
            doesItPass2 = True

    if not doesItPass1:
        sys.exit("Invalid file type")

    if not doesItPass2:
        sys.exit("Invalid type for new image")


def process_photo(): # Comments were used to help check process during testing
    try:
        shirt = Image.open("shirt.png")
        # print("Open Shirt Photo")
        imageData = Image.open(sys.argv[1])
        # print("Open Before Photo")
        imageData = ImageOps.fit(imageData, (600,600), Image.Resampling.BICUBIC, 0.0, (0.5,0.5)) 
        # print("Crop Before Photo")
            ## Got (600,600) from shirt.png and (0.5,0.5) from trial and error
        imageData.paste(shirt, (0, 0), shirt)
        # print("Overlay Photos")
        imageData.save(sys.argv[2])
        # print("Save New Photo")
    except:
        sys.exit("Unknown Error")
    
if __name__ == "__main__":
    main()