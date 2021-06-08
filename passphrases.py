rom random_word import RandomWords
import random


def limit_length():
    """
    Return a word limit as an integer if it's a number over 0 and below
    51, and the user doesn't want to quit.
    """
    while True:
        word_limit = input('Enter number of words in passphrase'
                           '\n(Limit is 50 words): ')
        valid_limit = list(range(1, 51))
        valid_limit = str(valid_limit)

        if word_limit in valid_limit:
            word_limit = int(word_limit)
            return word_limit
        elif word_limit == 'q':
            break
        else:
            print('*** Invalid syntax ***')


def get_word_spacer(word_limit):
    """
    Return a word spacer as long as the word limit exists and the user
    doesn't want to quit.
    """
    while word_limit:
        spacer = input('Enter a symbol to separate the words in your passphrase'
                       '\n(Hit space bar and enter for no symbols): ')
        if spacer == 'q':
            word_limit = False
        else:
            return spacer


def get_word_case(spacer, limit):
    """
    Generate a list of random words.
    Generate a random combination of a preferred number of those words.
    Join that combination with a preferred word spacer.
    Finally, print the result as a passphrase in a preferred word case
    as lon as the word spacer exists, the user chooses a valid word
    case option, and the user doesn't want to quit.
    """
    while spacer:
        rw = RandomWords()
        words = rw.get_random_words()

        random_combination = random.sample(words, limit)
        passphrase = spacer.join(random_combination)

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


def generate_passphrase():
    """
    Generate a passphrase with a word limit, a word spacer to
    separate the words, and a preferred word case formed of randomized
    words.
    """
    length = limit_length()
    word_spacer = get_word_spacer(length)

    get_word_case(word_spacer, length)
