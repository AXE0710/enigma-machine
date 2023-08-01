import string
import time
char = " " + string.punctuation + string.ascii_letters + string.digits 
char_list = list(char)
def change_key():
    global char_list
    global char
    global current_time
    var = int(1)
    var = var + int(current_time)
    while var>24:
        var = var - 24
    if var == 1:
        char = " " + string.punctuation + string.ascii_letters + string.digits
    elif var == 2:
        char = " " + string.ascii_letters + string.punctuation + string.digits
    elif var == 3:
        char = " " + string.ascii_letters + string.digits + string.punctuation
    elif var == 4:
        char = " " + string.digits + string.ascii_letters + string.punctuation
    elif var == 5:
        char = " " + string.digits + string.punctuation + string.ascii_letters
    elif var == 6:
        char = " " + string.punctuation + string.digits + string.ascii_letters
    elif var == 7:
        char = string.punctuation + " "  + string.ascii_letters + string.digits
    elif var == 8:
        char = string.ascii_letters + " " + string.punctuation + string.digits
    elif var == 9:
        char = string.ascii_letters + " " + string.digits + string.punctuation
    elif var == 10:
        char = string.digits + " " + string.ascii_letters + string.punctuation
    elif var == 11:
        char = string.digits + " " + string.punctuation + string.ascii_letters
    elif var == 12:
        char = string.punctuation + " " + string.digits + string.ascii_letters
    elif var == 13:
        char = string.ascii_letters + string.punctuation + " " + string.digits
    elif var == 14:
        char = string.ascii_letters + string.digits + " " + string.punctuation
    elif var == 15:
        char = string.digits + string.ascii_letters + " " + string.punctuation
    elif var == 16:
        char = string.digits + string.punctuation + " " + string.ascii_letters
    elif var == 17:
        char = string.punctuation + string.digits + " " + string.ascii_letters
    elif var == 18:
        char = string.ascii_letters + string.punctuation + string.digits + " "
    elif var == 19:
        char = string.ascii_letters + string.digits + string.punctuation + " "
    elif var == 20:
        char = string.digits + string.ascii_letters + string.punctuation + " "
    elif var == 21:
        char = string.digits + string.punctuation + string.ascii_letters + " "
    elif var == 22:
        char = string.punctuation + string.digits + string.ascii_letters + " "
    elif var == 23:
        char = string.ascii_letters + string.punctuation + string.digits + " "
    elif var == 24:
        char = string.ascii_letters + string.digits + string.punctuation + " "
    char_list = list(char)
    


t = time.localtime()
current_time = time.strftime("%H", t)

def encryption():
    password = input("Enter the text to be encrypted: ")
    passlist = list(password)
    change_key()
    for i in range(len(passlist)):
        passlist[i] = char_list.index(passlist[i])
        enctrpt = passlist[i] + int(current_time)
        if enctrpt > 94:
            enctrpt = enctrpt - 94
        passlist[i] = char_list[enctrpt]
    print("".join(passlist))


def decryption():
    password = input("Enter the text to be decrypted: ")
    passlist = list(password)
    change_key()
    for i in range(len(passlist)):
        passlist[i] = char_list.index(passlist[i])
        enctrpt = passlist[i] - int(current_time)
        if enctrpt < 0:
            enctrpt = enctrpt + 94
        passlist[i] = char_list[enctrpt]
    print("".join(passlist))

print("Welcome to the Encryption and Decryption Program")
print("Select the Encryption Key")
print("1. Month")
print("2. Day")
print("3. Hour")
option = input("Enter the option: ")
option = int(option)
if option == 1:
    current_time = time.strftime("%m", t)
elif option == 2:
    current_time = time.strftime("%d", t)
elif option == 3:
    current_time = time.strftime("%H", t)
else:
    print("Invalid Choice")
print("wants to encrypt or decrypt?")
print("1. Encrypt")
print("2. Decrypt")
choice = input("Enter the choice: ")
choice = int(choice)
if choice == 1:
    encryption()
elif choice == 2:
    decryption()
else:
    print("Invalid Choice")
