import re

from password_validation import password_validation
from email_validation import email_validation


def validation():

    def take_email():
        e_valid = False
        while e_valid == False:
            email = input('Enter your email: ')
            e_valid = email_validation(email)

        if e_valid == True: return True 
        else: return False


    def take_password():      
        p_valid = False
        while p_valid == False:
            password = input('Enter your password: ')
            p_valid = password_validation(password)
        
        if p_valid == True: return True 
        else: return False



    if take_email() and take_password() == True:
        return True
    else: return False



if __name__ == '__main__':
    if validation():
        print('Validation Complete!')