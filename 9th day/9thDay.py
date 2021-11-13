#Dictionaries [key, Value]

programming_dictionary = {
    "Bug": "An error in a program that prevents the program running as expected",
    "Function": "A piece of code that can easily call over and over again"
}

#Retrieving items from dictionary
print(programming_dictionary["Bug"])

#Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary
empty_dictionary = {}

#Wipe an excisting dictionary
programming_dictionary = {}

#Editing an excisting item in a dictionary
programming_dictionary["Bug"] = "Something else"

#Loop through a dictionary
for key in programming_dictionary:
    print(key, programming_dictionary[key])



#--------------------------------------------------------------
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
  if student_scores[key] > 90:
    student_grades[key] = "Outstanding"
  elif student_scores[key] > 80:
    student_grades[key] = "Exceeds Exceptions"
  elif student_scores[key] > 70:
    student_grades[key] = "Acceptable"
  else:
    student_grades[key] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)


#-------------------------------------------------------------------

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, numOfVisits, listOfCities):
  travel_log.append({
    "country": country,
    "visits": numOfVisits,
    "cities": listOfCities
  })

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



