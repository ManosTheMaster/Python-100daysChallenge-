#float
bill = float(input("What is the total bill? $"))
#int
tip = int(input("how much tip would you like to give? 10,15,20? "))
#int
people = int(input("How many people to split the bill? "))


totall_tip= bill*tip/100

bill_per_person = (bill + totall_tip)/people

print("Each person should pay: $" + str(bill_per_person))