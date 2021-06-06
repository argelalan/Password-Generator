from passwords import generate_password as gpw
from passwords import generate_passphrase as gpp


def password_generator():
    """Generate a random password or passphrase"""
    while True:
        user_prompt_1 = input("(Enter 'q' any time to quit)\n"
                              "1. Password\n2. Passphrase\nEnter '1' or '2': ")

        if user_prompt_1 == '1':
            gpw()
            break
        elif user_prompt_1 == '2':
            gpp()
            break
        elif user_prompt_1 == 'q':
            break
        else:
            print('*** Invalid syntax ***')


password_generator()
