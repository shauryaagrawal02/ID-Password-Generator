#IDPass Generator
#By Shaurya agrawal

print("make your own id pass generator")
import random
def generate_id():
    print("1.make your own ID")
    name = input("enter your first name ")
    ID = ""
    for i in range(4):
        ID += random.choice("0123456789")
        a = name+'@'+ID

    print("Your ID is:",a)

def generate_password():
    print("2.make your ID's password")
    len = int(input("enter the length of password "))

    print("which type of character do you want")
    print("L = Letters ")
    print("LN = Letters + Numbers ")
    print("LNS = Letters +Numbers + Symbols ")

    choice = input("Enter your choice (L/LN/LNS): ")
    letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    numbers = "987654321"
    symbols = "!@#$%^&*"
    #L stands for letters
    if choice == "L":
        char =letters
    #LN stands for letters plus numbers
    elif choice == "LN":
        char = letters +numbers
    #LNS Stands for letters plus numbers plus symbols
    elif choice == "LNS":
        char = letters +numbers+ symbols
    else:
        print("Invalid choice")
        return
    password = ""
    for i in range(len):
        password += random.choice(char)

    print("Your password is:", password)


generate_id()
generate_password()
