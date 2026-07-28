def main():
    m = input("m: ")
    print("E: " + str(convert_to_E(m)))

def convert_to_E(m):
    E = int(m) * (300000000 * 300000000)
    return E

main()