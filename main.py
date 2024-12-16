# Matthew hall
# December 16, 2024
# Password Validation Project
password = input('please enter your password: ')

def check_length():
    if len(password) <= 8:
        print('Your password must be 8 characters long!')
    else:
        print('Your Password is valid.')

def check_First_five():
    if len(password) >= 5 and password.isalpha():
        print('Your Password is valid.')
    else:
        print("The first five characters must be letters only!")

def check_last_three():
    if len(password) >= 3 and password.isdigit():
        print('Your Password is valid.')
    else:
        print("The last three characters must be numbers only!")




























