import re
import getpass

EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def welcome_msg():
    print('Welcome to Echtiat app!')

def request_email():
    email = input('Enter email address to sign-in [Type "C" to sign-up]: ')
    return email
    
def request_password():
    password = getpass.getpass('Password: ')
    return password

def check_email(email):
    return re.fullmatch(EMAIL_REGEX, email)    

def user_signin():
    welcome_msg()
    while True:
        email = request_email()
        if email == 'C':
            user_signup()
            continue
        if not check_email(email):
            print('Incorrect email address. Try again.')
            continue
        password = request_password()
        if confirm_user_account(email, password):
            print('Sign-in compeleted successfully!')
        else:
            print('User credentails are incorrect. Try again.')


def user_signup():
    while True:
        email = input('Enter your email address: ')
        password = request_password()
        password_repeat = getpass.getpass('Repeat the password: ')
        if password == password_repeat:
            #Write user details to DB
            print('Creating user account')
            break
        print('Passwords do not match. Try again') 

def confirm_user_account(email, password):
    print('Confirming user account...')
    return False
