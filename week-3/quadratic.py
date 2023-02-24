#solving a quadratic formula
#ax^2 + bx + c=0

a=int(input("Input a : "))
b=int(input("Input b:  "))
c=int(input("Input c : "))

#calculate the discriminant
d=(b**2) - (4*a*c)
x=7

#calculate the formula
solution_1=(-b + x/(2*a))
solution_2=(-b - x/(2*a))

print(solution_1)
print(solution_2)