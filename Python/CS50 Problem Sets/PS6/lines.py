import sys

# Feel free to use copies of some of my other Python scripts to test

def main():
    check_argv()
    process_count()

def check_argv():
    argv = len(sys.argv) - 1
    if argv < 1:
        sys.exit("Too few command-line arguments")
    elif argv > 1:
        sys.exit("Too many command-line arguments")

    if sys.argv[1].endswith(".py") == False:
            sys.exit("Not a Python file")
    
def process_count():
    data = []

    try:
        with open(sys.argv[1]) as file:
            for row in file:
                line = row.rstrip()
                if line != "" and line.__contains__("#") == False: # Removes empty lines and comments
                    data.append(line)

        print("# of lines in " + str(sys.argv[1]) + ": " + str(len(data)))
            
    except FileNotFoundError:
        sys.exit("File does not exist")
    except:
        sys.exit("Unknown error")
    
if __name__ == "__main__":
    main()