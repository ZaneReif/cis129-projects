# Module 6 Lab - Hot Dog Cookout Calculator
# Zane Reif
# 22 March 2024
# Calculates the minimum number of hot dogs and buns needed for a cookout

import math
def get_total_hot_dogs():
    # Input
    people = int(input('Enter the number of people attending the cookout: '))
    hot_dogs = int(input('Enter the number of hot dogs for each person: '))

    # Processing
    total = people * hot_dogs
    DOGS = 10
    BUNS = 8
    dogsLeft = (DOGS - total % DOGS) % DOGS
    mindogs = math.ceil(total / DOGS)
    bunsLeft = (BUNS - total % BUNS) % BUNS
    minbuns = math.ceil(total / BUNS)

    # Output
    print('Minimum packages of hot dogs needed:', mindogs)
    print('Minimum packages of hot dog buns needed:', minbuns)
    print('Hot dogs left over:', dogsLeft)
    print('Hot dog buns left over:', bunsLeft)

get_total_hot_dogs()
