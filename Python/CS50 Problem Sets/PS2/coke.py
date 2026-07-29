def main():
    cokeCost = 50

    while cokeCost > 0:
        print("Amount Due: " + str(cokeCost))
        user_input = input("Insert Coin: ")
        try:
            coin = int(user_input)
            if coin == 5 or coin == 10 or coin == 25:
                cokeCost = cokeCost - coin
            else: 
                pass
        except:
            print("Input Error")
    if cokeCost < 0:
        print("Change Owed: " + str(-cokeCost))

if __name__ == "__main__":
    main()