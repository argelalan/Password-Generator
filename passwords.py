from random_word import RandomWords
import random
import string


def generate_password():
    """
    Generate a password formed from randomized uppercase and lowercase
    letters, numbers, and symbols. Make it as long as the user wants.
    Print out the password.
    """
    while True:
        valid_nums = list(range(1, 95))
        valid_nums = str(valid_nums)

        length = input('Enter a password length:\n(The limit is 94): ')

        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        num = string.digits
        symbols = string.punctuation

        combination = upper + lower + num + symbols

        if length in valid_nums:
            length = int(length)

            random_combination = random.sample(combination, length)
            password = ''.join(random_combination)

            print(f'\nPassword:\n{password}')
            break
        elif length == 'q':
            break
        else:
            print('*** Invalid syntax')


def generate_passphrase():
    """
    Generate a passphrase formed from randomized words of the length
    the user chooses. Separate the words with the characters chosen.
    Print out the passphrase with the case of the user's choosing
    """
    length = int(input('Enter number of words in passphrase'
                       '\n(Limit is 50 words): '))
    spacer = input('Enter a symbol to separate the words in your passphrase'
                   '\n(Hit space bar and enter for no symbols): ')

    rw = RandomWords()
    words = rw.get_random_words()

    random_combination = random.sample(words, length)
    passphrase = spacer.join(random_combination)

    while True:
        case = input('1. Upper\n2. Lower\n3. Title'
                     '\nEnter a number for a case: ')

        if case == '1':
            print(f'\nPassphrase: \n{passphrase.upper()}')
            break
        elif case == '2':
            print(f'\nPassphrase: \n{passphrase}')
            break
        elif case == '3':
            print(f'\nPassphrase: \n{passphrase.title()}')
            break
        elif case == 'q':
            break
        else:
            print('*** Invalid syntax ***')
