
# CTI-110
# P2HW2-Tip, Tax, and Total
# James Jenkins
# June 19, 2018

# The program should ask the user to enter the charge for the food. It should then 
# calculate the amount of the tip and the amount for sales tax. (Assume 18% tip
# and 7% sales tax.) Display both of these amount as well as the total cost of the
# meal.

# Display both of amount as well as the total cost of the meal

foodCost =  float(input( " Please enter the foodCost of the food: " ) )

tipAmount = 0.18 * foodCost

salesTax = 0.07 * foodCost

total = foodCost + tipAmount + salesTax

print( " foodCost: $ " + format( foodCost, " ,.2f"),
" tipAmount: $ " + format( tipAmount, " ,.2f"),
" salesTax: $ " + format( salesTax, " ,.2f"),
" total: $ " + format( total, " ,.2f"),)

