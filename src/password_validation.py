import re

def password_validation(password):

    def language(password):
        return re.match(r"^[A-Za-z0-9]+$", password)

    def lenght(password):
        return len(password)

    def uppercase(password):
        return re.match(r'.*[A-Z]', password)
    
    def digit(password):
        return re.match(r'.*[0-9]', password)
         
    def special_character(password):
        return re.match(r'.*[@#$%^&!-()`~"+= ]', password)

    
    if special_character(password):
        print("Password should not contain any special characters")
        return False

    elif language(password) is None:
        print('Password must contain only english letters')
        return False

    elif lenght(password) < 8:
        print('Your password should be at least 8 characters')
        return False

    elif digit(password) is None:
        print('Password must contain at least one digit')
        return False

    elif uppercase(password) is None:
        print('Password must contain at least 1 uppercase character')
        return False

    else:
        return True
