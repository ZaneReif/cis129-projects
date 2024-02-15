#coffeeshop.py
#Zane Reif
"""Module 3 Lab Coffee Shop Simulator"""

#variables
name = input('Hello, what is your name? ') #input user name for receipt
print('Welcome, ' + name) #welcome message
print('Our Menu:\n'
      'Coffee: $5\n'
      'Muffin: $4\n'
      'Doughnut $3\n'
      'Cookie $2')
value1 = input('How many cups of coffee would you like to order? ') #value1 = number of coffees
value1 = int(value1) #convert value1 into integer
value2 = input('How many muffins would you like to order? ') #value2 = number of muffins
value2 = int(value2) #convert value2 into integer
value3 = input('How many doughnuts would you like to order? ') #value3 = number of doughnuts
value3 = int(value3) #convert value3 into integer
value4 = input('How many cookies would you like to order? ') #value4 = number of cookies
value4 = int(value4) #convert value4 into integer
coffeetotal = (value1*5.00) #calculate total cost of coffees
muffintotal = (value2*4.00) #calculate total cost of muffins
doughnuttotal = (value3*3.00) #calculate total cost of doughnuts
cookietotal = (value4*2.00) #calculate total cost of cookies
tax = ((value1*5.00)+(value2*4.00)+(value3*3.00)+(value4*2.00))*0.06 #calculate 6% tax on subtotal
total = (coffeetotal+muffintotal+doughnuttotal+cookietotal+tax) #calculate total

#receipt
print('\n'
      '***************************************\n'
      'My Coffee and Muffin Shop\n'
      'Number of coffees bought?')
print(value1)
print('Number of muffins bought?')
print(value2)
print('Number of Doughnuts bought?')
print(value3)
print('Number of Cookies bought?')
print(value4)
print('***************************************\n'
      '\n'
      '***************************************\n'
      'My Coffee and Muffin Shop Receipt:')
print(str(value1) + ' Coffee at $5 each: $ ' + str(coffeetotal)) #display coffee total
print(str(value2) + ' Muffins at $4 each: $ ' + str(muffintotal)) #display muffin total
print(str(value3) + ' Doughnuts at $3 each: $ ' + str(doughnuttotal)) #display doughnut total
print(str(value4) + ' Cookies at $2 each: $ ' + str(cookietotal)) #display cookie total
print('6% tax: $ ' + str(tax)) #display tax
print('-----')
print('Total: $ ' + str(total)) #display total
print('***************************************')
print('Thank you ' + name + ', come again!') #final appreciation message
