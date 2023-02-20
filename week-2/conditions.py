age= 24
gender="male"

if (age<16):
  print("you are still young")

else :
    print("should get an ID")

#compound / multiple conditions
if((age<30) & (gender == "male")):
    print("you qualify for a loan")
else:
    print("no loan for you")

fav_colour="black"
age =18
if (fav_colour == "black") | (age<=22):
    print("happy birthday to you")

else:
    print("no bithday for you")
