master_pwd = input("what is the master password? ")


def view():
    with open("passwords.txt", "r")as f:
        for line in f.readline():
            data=line.rstrip()
            user,passw=data.split("|")
            


def add():
    name = input("account name: ")
    pwd = input("password: ")

    with open("passwords.txt", "a")as f:
        f.write(name+" | "+pwd+"\n ")


while True:

    mode = input(
        "would you like to add a new password or vew existing ones (view,add) nad q for quit() : ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode.")
        continue
