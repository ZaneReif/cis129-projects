# Module 12 Lab
# Zane Reif
# 11 May 2024
# Displays the name, type, and age of a pet

def main():
    inputName = ''
    inputType = ''
    inputAge = 0

    Animal = Pet('', '', 0)

    print('Enter a pet name:')
    inputName = input()
    Animal.setName(inputName)

    print('Enter a pet type:')
    inputType = input()
    Animal.setType(inputType)

    print('Enter a pet age:')
    inputAge = int(input())
    Animal.setAge(inputAge)

    print('Your pet name:', Animal.getName())
    print('Your pet type:', Animal.getType())
    print('Your pet age:', Animal.getAge())

class Pet:
    def __init__(self, n, t, a):
        self.name = n
        self.type = t
        self.age = a

    def setName(self, n):
        self.name = n

    def setType(self, t):
        self.type = t

    def setAge(self, a):
        self.age = a

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getAge(self):
        return self.age

main()
