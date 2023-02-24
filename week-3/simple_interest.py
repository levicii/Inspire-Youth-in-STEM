#writee a program to calculate simple interest
def simple_interest(p, r ,t):
    simple_interest=(p * r * t)/100

p=float(input("enter the principal amount :"))
r=float(input("enter the rate of interest :"))
t=float(input("enter time of years :"))

#simpleinterest =(p * r * t)/100

print("simple interest is:",simple_interest)