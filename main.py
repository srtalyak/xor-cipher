def XORencoding():
    text = input("Please enter your text for encoding: ")
    key = input("Please enter the key for encoding: ")
    print("\nEncoding...\n")

    encoded = []
    for charText, charKey in zip(text, key * len(text)):
        encoded.append(ord(charText) ^ ord(charKey))
    print("""Encrypted text is:\n{}\n""".format(encoded))


def XORdecoding():
    while True:
        try:
            array = input("Please enter your ASCII array for decoding: ")
            array = array.split(",")
            for i in array:
                int(i)
        except ValueError:
            print("\nPlease enter a valid ASCII array!")
        else:
            break

    key = input("Please enter the key for decoding: ")
    print("\nDecoding...\n")

    decoded = ""
    for itemArray, charKey in zip(array, (key * len(array))):
        decoded += chr(int(itemArray) ^ ord(charKey))
    print("""Decrypted text is:\n{}\n""".format(decoded))


def main():
    while True:
        print("""\nWelcome to XOR encode/decode program
        1- Encode
        2- Decode
        
        """)
        choice = input("Select a choice(1-2): ")
        if choice == "1":
            XORencoding()
        elif choice == "2":
            XORdecoding()
        else:
            print("Please make a valid choice!\n")
        choice = input("Do you want to continue(y/n): ")
        if choice == "y" or choice == "":
            continue
        else:
            print("goodbye...")
            break


main()
