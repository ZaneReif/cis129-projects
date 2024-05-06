# Module 10 Lab - Check Formatting
# Zane Reif
# 25 April 2024
# Ensures a check amount has 10 characters using asterisks

def check_amount(amount):
    balance = (f'{amount:*>10}')
    return balance

dollar_amount = (input('Enter the dollar amount: $'))

balance = check_amount(dollar_amount)
print(f'Protected Amount: ${balance}')
