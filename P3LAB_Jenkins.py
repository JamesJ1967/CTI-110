# Jenkins
# Ensure this progam is corrected and will run properly without
# any errors.
# This program takes a number grade and outputs a letter grade.
# system uses 10-point grading scale
# TO DO: define the rest of the scores
# TO DO: finish this
# program start

def main (): 

  A_score = 90 - 100
  B_score = 80 - 89
  C_score = 70 - 79
  D_score = 60 - 69
  F_score = 0 - 60
             
grade = int(input("Enter a score grade from 0 to 100: "))

if grade > 89 and grade < 101:
    print("You score an A!")
    print("Your score is an A!")
elif grade > 79 and grade < 90:
    print("You score an B!")
    print("Your score is an B!")
elif grade > 69 and grade < 80:
    print("You score an C!")
    print("Your score is an C!")
elif grade > 59 and grade < 70:
    print("You score an D!")
    print("Your score is an D!")
elif grade >= 0 and grade < 60:
    print("You score an F!")
    print("Your score is an F!")
else:
    print("score enter incorrectly Not working Redo")








