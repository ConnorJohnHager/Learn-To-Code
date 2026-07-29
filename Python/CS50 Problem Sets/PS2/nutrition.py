def determine_calories(input):
    input = input.lower().strip()

    foods = {
        "apple" : 130,
        "avocado" : 50,
        "banana" : 110,
        "cantaloupe" : 50,
        "grapefruit" : 60,
        "grapes" : 90,
        "honeydew melon" : 50,
        "kiwifruit" : 90,
        "lemon" : 15,
        "lime" : 20,
        "nectarine" : 60,
        "orange" : 80,
        "peach" : 60,
        "pear" : 100,
        "pineapple" : 50,
        "plums" : 70,
        "strawberries" : 50,
        "sweet cherries" : 100,
        "tangerine" : 50,
        "watermelon" : 80
    }

    if input in foods:
        return "Calories: " + str(foods[input])
    else:
        return "Not found"

    # I added this if-statement to inform the user if there was an error

def main():
    user_input = input("Item: ")
    print(determine_calories(user_input))

if __name__ == "__main__":
    main()