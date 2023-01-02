name=input("Type Your name: ")
print("welcome",name.capitalize(),"to this adventure")

answer= input("You are on a dirt roade,it has come to an end and you can go left or right: ").lower()

if answer=="left":
    answer=input("You come to a river ,you can walk around it or swim accrose the river: ").lower()

    if answer=="swim":
        answer=input("font of your have a Bear,What do you want?(Run or acct like death): ").lower()

        if answer=="death":
            print("you do wright thing you are alive")
        if answer=="run":
            print("Sorry the Bear grab you !")
    if answer=="walk":
        print("Owao you reach tha gold hill")
    else:
        print("Not a valid option. you lose.")

elif answer == "right":
    print()
else:
    print("Not a valid option. You lose!")