# FuelApp
# This program calculates total litres of fuel served to a customer
# The computation is done using price/litre and purchased amount as input

pricePerLitre = 8.59    # Price per litre of fuel in GHS as set by OMC, stored in variable

print('Welcome to GOIL FuelApp! Please enter the amount of fuel you wish to purchase.') # Welcome message asks for user input

amountPurchased = input()   # Program takes user input here as str

litresDispensed = int(amountPurchased) / pricePerLitre  # Python converts str input to int then Divides input by pricePerLitre

litresDispensed = round(litresDispensed, 2) # round() rounds resultant float in line 10 to 2 decimal places

print('Thank you for your purchase. You have been served' + ' ' + str(litresDispensed) + ' ' + 'litres of premium unleaded fuel.')
# str() converts rounded value in line 15 to str
# Concatenate all strs
# Displays volume of fuel served to customer
