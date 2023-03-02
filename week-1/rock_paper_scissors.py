import random
user_wins=0
computer_wins=0
options=("rock","paper","scissors")
options[0]

while True:
    user_input=input("type rock/paper/scissors or Q to quit.").lower()
    if user_input=="q":
        break

    if user_input  not in ("rock ","paper","scissors"):
        continue

random_number= random.randint(0,2)
#rock:0, paper: 1, scissors: 2
computer_pick=options[random_number]
print("computer picked",computer_pick + ".")

if user_input=="rock" and computer_pick=="scissors":
    print("you win !")
    user_wins += 1


    if user_input=="paper" and computer_pick=="rock":
     ("you win")

print("Gooodbye!")


