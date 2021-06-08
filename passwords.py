import random
import string


def generate_password():
    """
    Generate a password formed from randomized uppercase and lowercase
    letters, numbers, and symbols. Make it as long as the user wants.
    Print out the password.
    """
    while True:
        valid_lengths = list(range(1, 95))
        valid_lengths = str(valid_lengths)

        length = input('Enter a password length:\n(The limit is 94): ')

        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        num = string.digits
        symbols = string.punctuation

        combination = upper + lower + num + symbols

        if length in valid_lengths:
            length = int(length)

            random_combination = random.sample(combination, length)
            password = ''.join(random_combination)

            print(f'\nPassword:\n{password}')
            break
        elif length == 'q':
            break
        else:
            print('*** Invalid syntax ***')
