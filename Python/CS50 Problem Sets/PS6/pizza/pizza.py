import sys
from tabulate import tabulate

# Remember to input 'python -m pip install tabulate' in your terminal to be able to import

def main():
    check_argv()
    process_menu()

def check_argv():
    argv = len(sys.argv) - 1
    if argv < 1:
        sys.exit("Too few command-line arguments")
    elif argv > 1:
        sys.exit("Too many command-line arguments")

    if sys.argv[1].endswith(".csv") == False:
            sys.exit("Not a CSV file")
    
def process_menu():
    data = []

    try:
        with open(sys.argv[1]) as file:
            for row in file:
                pizzaType = row.rstrip().split(",")
                data.append(pizzaType)

            print(tabulate(data, headers="firstrow", tablefmt="grid"))
            
    except FileNotFoundError:
        sys.exit("File does not exist")
    except:
        sys.exit("Unknown error")
    
if __name__ == "__main__":
    main()