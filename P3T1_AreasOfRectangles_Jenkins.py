# CTI- 110
# P3T1- Area of Rectangles
# James Jenkins

# Write a program that asks for the length and width of two rectangles.
# The program should tell the user which rectanggle has the greater area
# or if the two rectangles have equal area.

# The area of a rectangle is its length multiplied by its width.

# This program's logic should have three branches:
# 1.The first rectangle has the larger area
# 2. The second rectangle has the larger area
# 3.Both rectangles have equal area

RectangleOneLength=float(input("Please enter the length of rectangle 1:"))
RectangleOneWidth=float(input("Please enter the width of rectangle 1:"))
RectangleTwoLength=float(input("Please enter the length of rectangle 2:"))
RectangleTwoWidth=float(input("Please enter the width of rectangle 2:"))   
RectangleOneArea =RectangleOneLength *RectangleOneWidth
RectangleTwoArea =RectangleTwoLength *RectangleTwoWidth

if RectangleOneArea > RectangleTwoArea:
    print("Rectangle One is larger than Rectangle Two" )
elif RectangleTwoArea > RectangleOneArea:
    print("Rectangle Two is larger than Rectangle One" )
else:
    print ("Both Rectangles are equal " )
