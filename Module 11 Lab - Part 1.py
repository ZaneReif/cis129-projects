# Module 11 Lab - Part 1
# Zane Reif
# 5 May 2024
# Saves a list of grades to file grades.txt

# Section 9.1
with open ('grades.txt', mode='w') as grades:
    while True:
        grade = input('Enter a grade (enter -1 to quit): ')
        if grade == '-1':
            break
        grades.write(grade + '\n')

print ('Grades have been saved to grades.txt')
