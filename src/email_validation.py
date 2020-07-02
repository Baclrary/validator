import re

pattern_email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

valid_domens = [
    "gmail.com",
    "outlook.com",
    "yahoo.com",
    "icloud.com",
    "aol.com",
    "mail.ru",
    "ukr.net"
]

def email_validation(email):

    def characters(email):
        valid = pattern_email.search(email)
        return valid


    def domain(email):
        take_domain = email.split("@")

        if take_domain[1] not in valid_domens:
            print(f"Sorry, we do not support \"{take_domain[1]}\" domain.")
            return False
        else: return True




    if characters(email) is None:
        print('Email format is invalid.')
        return False

    elif domain(email) == False:
        return False

    else:
        return True
