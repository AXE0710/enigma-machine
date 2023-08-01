from tkinter import *
import string
import time
root = Tk()
root.title("Enigma Machine")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg="black")
heading = Label(root, text="Enigma Machine", font=("Helvetica", 20), bg="black", fg="white")
heading.pack()
info = Label(root, text="Enter the text to be encrypted or decrypted", font=("Helvetica", 15), bg="black", fg="white")
info.pack(pady=10)
status = StringVar()
status.set("ENTER")
password_status = Label(root, textvariable=status, font=("Helvetica", 15), bg="black", fg="white")
password_status.pack(pady=10)

password_entry = Entry(root, font=("Helvetica", 15), bg="black", fg="white")
password_entry.pack(pady=10)

# set of characters
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
    password = password_entry.get()
    passlist = list(password)
    change_key()
    for i in range(len(passlist)):
        passlist[i] = char_list.index(passlist[i])
        enctrpt = passlist[i] + int(current_time)
        if enctrpt > 94:
            enctrpt = enctrpt - 94
        passlist[i] = char_list[enctrpt]
    password_entry.delete(0, END)
    password_entry.insert(0, "".join(passlist))
    status.set("Encrypted")


def decryption():
    password = password_entry.get()
    passlist = list(password)
    change_key()
    for i in range(len(passlist)):
        passlist[i] = char_list.index(passlist[i])
        enctrpt = passlist[i] - int(current_time)
        if enctrpt < 0:
            enctrpt = enctrpt + 94
        passlist[i] = char_list[enctrpt]
    password_entry.delete(0, END)
    password_entry.insert(0, "".join(passlist))
    status.set("Decrypted")




def option():
    op = var.get()
    global current_time
    t = time.localtime()
    if op == 1:
        current_time = time.strftime("%m", t)
    elif op == 2:
        current_time = time.strftime("%d", t)
    elif op == 3:
        current_time = time.strftime("%H", t)


    
select = Label(root, text="Select the Encryption Key", font=("Helvetica", 15), bg="black", fg="white")
select.pack(pady=10)
# options
var = IntVar()
option1 = Radiobutton(root, text="Month",variable=var,font=("Helvetica", 15),bg="gray30",value=1, command=option)
option1.pack(pady=10)
option2 = Radiobutton(root, text="Day",variable=var,font=("Helvetica", 15),bg="gray30",value=2, command=option)
option2.pack(pady=10)
option3 = Radiobutton(root, text="Hour",variable=var,font=("Helvetica", 15),bg="gray30",value=3, command=option)
option3.pack(pady=10)


submit_button = Button(root, text="Encypt", font=("Helvetica", 15), bg="black", fg="white", command=encryption)
submit_button.pack(pady=10)
decryption_button = Button(root, text="Decrypt", font=("Helvetica", 15), bg="black", fg="white", command=decryption)
decryption_button.pack(pady=10)



root.mainloop()
