from random import randint
from math import sqrt

MIN_NUMBER = 1
MAX_NUMBER = 100
PRIME_DESCRIPTION = 'Answer "yes" if given number is prime.'\
                    ' Otherwise answer "no".'


def run_prime():
    number_to_quess = randint(MIN_NUMBER, MAX_NUMBER)
    if is_prime(number_to_quess):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number_to_quess, correct_answer


def is_prime(number):
    if number < 2:
        return False
    max_divisor = int(sqrt(number) + 1)
    for divisor in range(2, max_divisor):
        if number % divisor == 0:
            return False
    return True
