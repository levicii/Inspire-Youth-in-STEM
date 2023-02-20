#!/usr/bin/env python3

myFavouriteFruits=["banana","apple","orange","pawpaw"]
for fruit in myFavouriteFruits:
    print(fruit)

    print (len(myFavouriteFruits))
    #len=number of elements in the list

friends=["levis","dante","johnny","vergil"]
print(friends)
friends[0]="levicii"
print(friends)
print("-----------------------------------------------------------")
new_friends=friends.copy()
print(new_friends)
new_friends.sort()
print(new_friends)

new_friends.pop()
print(new_friends)








#append()=>adds an element at the end of the list
#clear()=>tremoves all the elements in a list
#copy()=>copies all elements in another list
#insert()=>adds an element to a specified position
#reverse()=>reverses the order of the list
#sort()=>puts the list in alphabetical order
#pop()=>removes the element of a specified position
#count()=>returns the number within the specified list
