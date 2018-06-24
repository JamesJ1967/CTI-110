# CTI-110
# P3HW1 - Age Classifier
# James Jenkins
# 062218

# write a program that asks the user to enter a person's age
# The person should display a message indicating whether
# the person is an infant, a child, a teenager, or an adult.

# Follow these guidelines:

# if the person is 1 year old or less, he or she is an infant
# if the person is older than old year, but younger than 13 years,
# he or she is a child
# if the person is at least 13 years old, but less than 20 years
# old, he or she is a teenager.
# if the person is at least 20 years old, he or she is an adult.

userAge = int( input( "Please user your age: " ))
if userAge  <= 1:
     print( "the user is an infant" )
elif userAge < 13:
     print( "the user is an child" )
elif userAge < 20:
     print( "the user is an teenager" )
else:
    print( "the user is an adult" )           
