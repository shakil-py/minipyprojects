print("Welcome to ay computer quize")

playing = input("Do you want to play? ")
# print(playing)
if playing.lower() != "yes":
    quit()
print("okay let's play")
socre = 0
answer = input("What dose CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct !")
    socre+=1
else:
    print("Incorrect !")

answer = input("What dose Graphics Card stand for? ")
if answer.lower() == "grafical processing unit":
    print("Correct !")
    socre+=1
else:
    print("Incorrect !")

answer = input("What dose RAM stand for? ")
if answer.lower() == "random accesse memory unit":
    print("Correct !")
    socre+=1
else:
    print("Incorrect !") 
print("You got "+ str(socre)+" question correct !")
print("you got "+str((socre/4)*100)+"%.")
