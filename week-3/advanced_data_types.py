# #Mutable vs immutable
# #mutable are data types that can be edited during program life cycle
# #add or remove elements 
# #immutable-->Data types that cannot be edited during program life cycle
# #1 list(mutable)
# friends=("kendy","mitchelle","ivar")
# #or friends[] for 
# #add--> append(),extend()
# students=("marie","bryan","joy","faith")
# friends.extend("mary")
# friends.append("john")
# friends.sort()
# #2 Tuples(immutable)
# #type of list that is immutable
# stationeries=("pens","ink","sharpener")
# #replace the whole tuples 
# stationeries=("ruler","pencil")
# for stationery in stationeries:
#  print(stationery)

# numbers=(1,2,3,4,5,6,7,8,9,10)
#3 Dictionaries
#uses key and value pair

student={"Name": "levicii","gender":"female","age":23}
print(student["Name"])
print(student["age"])
print(student["gender"])
print(student.values())
print(student.keys())
#"name ":"levicii"-->name(key)levicii(value)

friend={"name :  " "fav_colour":"black","hobby":"swimming""course:law","weight":"65kg","height":"6.21ft"}
print(friend["name"])
print(friend["fav_colour"])
print(friend["hobby"])
print(friend["course"])
print(friend["weight"])
print(friend[""])