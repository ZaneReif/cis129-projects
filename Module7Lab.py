# Module 7 Lab - Theater Seating Program
# Zane Reif
# 1 April 2024
# Calculates theater income by number of seats sold

# Declare variables
sections = ['A', 'B', 'C']
seats = {'A': 300, 'B': 500, 'C': 200}
prices = {'A': 20, 'B': 15, 'C': 10}

# Welcome function
def welcome():
    print(f'Welcome to the Theater Seating program.\n')
    print(f'We have the following sections: {sections}.')
    print(f'Each section has the following number of seats: {seats}.')
    print(f'Seats in each section cost the following: {prices}.\n')

# Tickets sold function
def get_ticketsSold(sectionName):
    while True:
        ticketsSold = int(input(f'Enter number of tickets sold for section {sectionName}: '))
        if ticketsSold < 0:
            print(f'Number must be at least 0.\n')
        elif ticketsSold > seats[sectionName]:
            print(f'Number cannot be greater than {seats[sectionName]}.\n')
        else:
            return ticketsSold
        
# Subtotal function
def get_subtotal(sectionName, ticketsSold):
    return ticketsSold * prices[sectionName]

# Main function
def main():
    welcome()
    totalIncome = 0
    sectionTotals = {}
    for sectionName in sections:
        ticketsSold = get_ticketsSold(sectionName)
        subtotal = get_subtotal(sectionName, ticketsSold)
        totalIncome += subtotal
        sectionTotals[sectionName] = (ticketsSold, subtotal)
        print(f'Subtotal for section {sectionName}: ${subtotal}')
        print(f'Total so far: ${totalIncome}\n')

    print('Subtotals:')
    for sectionName in sections:
        ticketsSold, subtotal = sectionTotals[sectionName]
        print(f'Section {sectionName}: {ticketsSold} tickets were sold, subtotal: ${subtotal}')
    print(f'\nTotal Income: ${totalIncome}')

# Call main function
main()
