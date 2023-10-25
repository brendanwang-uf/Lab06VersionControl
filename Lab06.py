def encode(password):
    encoded_password = '' #empty string for password
    for value in password:
        new_value = (int(value) + 3) % 10  #shifts each digit up by 3 & wraps around the 10
        encoded_password += str(new_value)
    return encoded_password


def decode(encoded_password):
    decoded_password = ""
    for value in encoded_password:
        orig_digit = (int(value) - 3) % 10  #subtract 3 from each digit
        decoded_password += str(orig_digit)
    return decoded_password


def main():
    while True == True: #loops the menu
        print("""
Menu
-------------
1. Encode
2. Decode
3. Quit
    """)

        menu_option = input("Please enter an option: ")

        if menu_option == "1":
            password = input("Please enter your password to encode: ") #asks for initial password
            encoded_password_storage = encode(password)
            print("Your password has been encoded and stored!")

        if menu_option == "2":
            decoded_password_storage = decode(encoded_password_storage)
            print(f"The encoded password is {encoded_password_storage}, and the original password is {decoded_password_storage}.")
            pass

        if menu_option == "3":
            break #Quits the menu

if __name__ == "__main__":
    main()
