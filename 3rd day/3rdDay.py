# Check if a number is Even or Odd
number = int(input("Which number do you want to check? "))
if number % 2 == 1:
  print("Odd")
else:
  print("Even")

#BMI progmramm
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / (height**2)
bmi = bmi.__round__(1)
print("Your BMI is " + str(bmi) + " and you are ")

if bmi <= 18.5:
  print("underweight")
elif bmi < 25:
  print("normal")
elif bmi < 30:
  print("slightly overweight")
elif bmi < 35:
  print("obese")
else:
  print("clinically obese")


#Check if a year is a Leap
year = int(input("Which year do you want to check? "))

if (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)):
  print("Leap")
else:
  print("Not Leap")


#Roler coaster ticket
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")




#pizza order
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if  size == "S":
  bill += 15
  if add_pepperoni == "Y":
    bill += 2
elif size == "M":
  bill +=20
  if add_pepperoni == "Y":
    bill += 3
else:
  bill += 25
  if add_pepperoni == "Y":
    bill += 3


if extra_cheese == "Y":
  bill += 1

print("Your bill is " + str(bill))


#True Love finder
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1 = name1.lower()
name2 = name2.lower()

#TRUE LOVE 
t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")

l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e = name1.count("e") + name2.count("e")

valueOfLove = int(str(t + r + u + e) + str(l + o + v + e))
message = "Your score is " + str(valueOfLove) + ", "
if valueOfLove < 10 or valueOfLove > 90:
  message += "you go together like coke and mentos."
elif valueOfLove < 50 and valueOfLove > 40:
  message += "you are alright together."

print(message)