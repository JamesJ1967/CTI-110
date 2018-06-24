# CTI - 110
# P3HW2- Software Sales
# James Jenkins
# 062218

# A software company sells a package that retails for $99.
# They offer bulk discounts for volume purchases
# (for example, buying many copies to install in a college
# classroom).

# The discounts are as follows:

# Quantity 10-19: 	10% discount
# Quantity 20-49:	20% discount
# Quantity 50-99:	30% discount
# Quantity 100+:	40% discount

# Write a program that asks the user to enter the number  
# of packages purchased.The program should then display  
# the amount of the discount(if any) and the total purchase
# cost withdiscount applied.


userNumberOfPackage = int( input( " Please enter the number of package purchased: " ) )

packagePrice = 99

if  userNumberOfPackage < 10:
    discount = 0; 
elif userNumberOfPackage < 20:
     discount = 0.10
elif userNumberOfPackage < 50:
     discount = 0.20
elif userNumberOfPackage < 100:
     discount = 0.30
else:
     discount = 0.40
    
subTotal = userNumberOfPackage * packagePrice
discountAmount = discount * subTotal
total = subTotal - discountAmount


print( "Amount of discount: $" + format( discountAmount,",.2f"))
print( "Total amount: $" + format( total,",.2f")) 
     
                             

