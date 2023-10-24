#Brendan Wang

def encode(password):
    encoded_password = '' #empty string for password
    for value in password:
        new_value = (int(value) + 3) % 10  #shifts each digit up by 3 & wraps around the 10
        encoded_password += str(new_value)
    return encoded_password

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
            password = input("Please enter your password to encode: ") #asks for intial password
            encoded_password_storage = encode(password)
            print("Your password has been encoded and stored!")
            pass

        if menu_option == "2":
            #decode
            pass

        if menu_option == "3":
            break #Quits the menu

if __name__ == "__main__":
    main()
