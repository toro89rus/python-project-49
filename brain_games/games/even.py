from random import randint


def even():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    number_to_quess = randint(MIN_NUMBER, MAX_NUMBER)
    if is_even(number_to_quess):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number_to_quess, correct_answer


def is_even(number):
    return number % 2 == 0
