#write a program that calculates 16% tax on income
#ranging between 100k-150k

#19% tax income is between 150k-300k
#30% Tax income is above 300k
#15% if income is less than 100k
#print gross income ,net income



gross_input=int(input("what is your gross income:"))
taxgroup_1=(gross_input * 0.15)
taxgroup_2=(gross_input * 0.16)
taxgroup_3=(gross_input * 0.19)
taxgroup_4=(gross_input * 0.30)

if gross_input <=100000 :
    print ("gross_income:",gross_input)
    print("tax:",taxgroup_1)
    print("net_income:",gross_input - taxgroup_1)

elif (gross_input (int>= 100001)) & (gross_input< 150000):
    print("gross_income:",gross_input)
    print ("tax :",taxgroup_2)
    print("net_income:",gross_input-taxgroup_2)

elif (gross_input>=150001) & (gross_input<=300000):
    print("gross_income:",gross_input)
    print ("tax :",taxgroup_3)
    print("net_income :",gross_input-taxgroup_3)

elif (gross_input>=300001) :
    print("gross_income:",gross_input)
    print ("tax :",taxgroup_4)
    print("net-income:",gross_input-taxgroup_4)

