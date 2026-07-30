def collect_grocery_list():
    groceries = {
    }

    while True:
        try:
            item = input().strip().upper()
        
            if item != "":
                if groceries.__contains__(item):
                    groceries[item] += 1
                else:
                    groceries[item] = 1
            else:
                break
        except EOFError:
            break

        # EOFError is triggered differently between Mac and Windows
        # I added another condition to trigger finalizing the list
    
    print("Here's your grocery list!")
    for key in sorted(groceries):
        print(str(groceries[key]) + " " + str(key))

def main():
    print("Create your grocery list! Hit enter on a blank line to finalize list.")
    collect_grocery_list()

if __name__ == "__main__":
    main()