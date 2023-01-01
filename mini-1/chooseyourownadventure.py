name=input("Type Your name: ")
print("welcome",name.capitalize(),"to this adventure")

answer= input("You are on a dirt roade,it has come to an end and you can go left or right: ").lower()

if answer=="left":
    answer=input("You come to a river ,you can walk around it or swim accrose the river: ").lower()

    if answer=="swim":
        print()
    if answer=="walk":
        print()
    else:
        print("Not a valid option. you lose.")

elif answer == "right":
    print()
else:
    print("Mot a valid option. You lose!")