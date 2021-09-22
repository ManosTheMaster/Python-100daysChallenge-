#Loops

#For loop
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)

#Average student heights
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum = 0
numberOfStudents = 0
for height in student_heights:
  sum += height
  numberOfStudents += 1
if numberOfStudents != 0:
  print("The average height is " + round(sum/numberOfStudents))

#Highest score of students

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest = student_scores[0]

for score in student_scores:
  if score > highest:
    highest = score

print(f"he highest score in the class is: {highest}")


#Gauss Math problem
total = 0
for number in range(1, 101):
  total += number

print(total)

#Gauss Math problem with only the even number
total = 0
for number in range(2, 101, 2):
  total += number
print(total)

#FizzBuzz game

#Fizz 3
#Buzz 5
#FizzBuzz 15

for number in range(1,101):
  if (number % 3 == 0) and (number % 5 == 0):
    print("FizzBuzz")
  elif(number % 3 == 0):
    print("Fizz")
  elif(number % 5 == 0):
    print("Buzz")
  else:
    print(number)


