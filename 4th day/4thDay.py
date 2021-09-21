#Randomness
import random

random_int = random.randint(0,1)

if random_int == 0:
  print("heads")
else:
  print("tails")


#python list

states_of_America = ["Delaware", "Penssylvania", "Alaska", "Georgia", "New Jersey", "Arisona", "New Mexico"]
print(states_of_America[0]) #first index of the list
print(states_of_America[-1]) #last index of the list

#Who is gonna pay GAME
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

length = len(names)
print(random.randint(0,length))

print(f"{names[random.randint(0,len(names)-1)]} is going to pay")