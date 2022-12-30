import random
top_of_range=input("Type a number: ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range<=0:
        print("Please type a number larger than 0 next time.")
else:
    print("Please type a number next time.")
    quit()
random_number = random.randint(0,top_of_range)

while True:
    user_ges=input("Make A Guess")
    if user_ges.isdigit():
        user_ges=int(user_ges)
    else:
        print("Please type anumber next time.")
        continue
    if user_ges==random_number:
        print("You got it!")
        break
    else:
        print("You got it wrong !")
    
