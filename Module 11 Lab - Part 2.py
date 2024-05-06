# Module 11 Lab - Part 2
# Zane Reif
# 5 May 2024
# Prints the grades in grades.txt and calculates the average

# Section 9.2
with open('grades.txt', mode='r') as gradestxt:
    grades = [float(line.strip()) for line in gradestxt]

print('Individual Grades:')
for grade in grades:
    print(grade)

total = sum(grades)
count = len(grades)
average = total / count

print('\nTotal:', total)
print('Count:', count)
print('Average:', average)
