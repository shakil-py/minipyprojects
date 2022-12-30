print("Welcome to ay computer quize")

playing = input("Do you want to play? ")
# print(playing)
if playing.lower() != "yes":
    quit()
print("okay let's play")
answer = input("What dose CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct !")
else:
    print("Incorrect !")

answer = input("What dose Graphics Card stand for? ")
if answer.lower() == "grafical processing unit":
    print("Correct !")
else:
    print("Incorrect !")

answer = input("What dose RAM stand for? ")
if answer.lower() == "random access processing unit":
    print("Correct !")
else:
    print("Incorrect !")
