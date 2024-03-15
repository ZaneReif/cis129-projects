# CIS129_ZaneReif_Lab5.py
# Zane Reif
# 15 March 2024
# This program calculates weekly bottles and the total payout

# declare variables
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = 'y'

# calculate data
while keepGoing == 'y':
    counter = 1
    totalBottles = 0
    totalPayout = 0
    for counter in range(7):
        counter += 1
        todayBottles = (int(input(f'Enter number of bottles for day #{counter}: ')))
        totalBottles += todayBottles
        totalPayout = totalBottles * 0.10

    print(f'The total number of bottles collected is {totalBottles}')
    print(f'The total paid out is ${totalPayout: .2f}')

    keepGoing = (input("Do you want to enter another week's worth of data? (Enter y or n): "))

