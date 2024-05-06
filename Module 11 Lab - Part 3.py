# Module 11 Lab - Part 3
# Zane Reif
# 5 May 2024
# Saves 3 exam scores for each student in grades.csv

# Section 9.3
import csv

with open('grades.csv', mode='w', newline='') as gradescsv:
    writer = csv.writer(gradescsv)
    writer.writerow(['First Name', 'Last Name', 'Exam 1 Grade', 'Exam 2 Grade', 'Exam 3 Grade'])

    while True:
        firstname = input('Enter first name (enter -1 to quit): ')
        if firstname == '-1':
            break
        lastname = input('Enter last name: ')

        while True:
            try:
                exam1grade = int(input('Enter grade for exam 1: '))
                exam2grade = int(input('Enter grade for exam 2: '))
                exam3grade = int(input('Enter grade for exam 3: '))
                break
            except ValueError:
                print('Please enter a valid grade.')

        writer.writerow([firstname, lastname, exam1grade, exam2grade, exam3grade])

print('Grades have been successfully saved to grades.csv')
