import sys
import csv

def main():
    check_argv()
    process_data()
    print("Data Processed")

def check_argv():
    argv = len(sys.argv) - 1
    if argv < 2:
        sys.exit("Too few command-line arguments")
    elif argv > 2:
        sys.exit("Too many command-line arguments")
    
def process_data():
    data = []

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last, first = row["name"].split(", ")
                data.append({"first": first, "last": last, "house": row["house"]})
    except:
        sys.exit("Could not read " + str(sys.argv[1]))

    try:
        with open(sys.argv[2], "w", newline="") as newFile:
            fieldnames = ["first", "last", "house"]
            writer = csv.DictWriter(newFile, fieldnames=fieldnames)
            writer.writeheader()
            for each in data:
                writer.writerow({"first": each["first"], "last": each["last"], "house": each["house"]})
    except:
        sys.exit("Could not write " + str(sys.argv[2]))

if __name__ == "__main__":
    main()