#create a empty list of favourite musicians=[]
#using for loops addd five new musicians
#copy to a new list called celebs
#sort the list 
#pop out two celebrities
#count the remaining celebs

myFavouritemusians=[]
myFavouritemusians.append("drake")
myFavouritemusians.append("21 savage")
myFavouritemusians.append("young dolph")
myFavouritemusians.append("xxxtentacion")
myFavouritemusians.append("lil durk")
print(myFavouritemusians)

celebs=myFavouritemusians.copy()
print(celebs)

myFavouritemusians.sort()
print(myFavouritemusians)

myFavouritemusians.pop()
myFavouritemusians.pop()
print(myFavouritemusians)

counts=[myFavouritemusians.count(musicians)for musicians in myFavouritemusians]
print(counts)