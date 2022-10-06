from cryptography.fernet import Fernet


'''
# This function creates key.key file. Comment out these lines once key.key file is created
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:  # It will write in binary mode, Binary mode: deals with non-textual data
        key_file.write(key)


write_key()
'''


def load_key():
    file = open("key.key", "rb")  # read in binary mode
    key_key = file.read()
    file.close()
    return key_key  # open(), close()


key = load_key()
fer = Fernet(key)    # Initialize encryption module


def add():
    name = input("Please enter your account name: ")
    pwd = input("Please enter a new password: ")
    with open("passwords.txt", "a") as file:
        file.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        # go to the next line using carriage return


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():  # readlines(), return each line in a list
            data = line.rstrip()  # rstrip(), to remove the carriage return
            user_name, user_pwd = data.split("|")      
            print("User name: ", user_name, " | Password: ", fer.decrypt(user_pwd.encode()).decode())
            # encode(): convert string into byte string,  b'hello'
            # decode(): the reverse


while True:
    answer = input("Which mode would you like to use (view, add) or Q to quit: ").lower()
    if answer == "q":
        break

    if answer == "view":
        view()
    elif answer == "add":
        add()
    else:
        print("Not a valid option, please enter again")
        continue
