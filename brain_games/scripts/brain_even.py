#!/usr/bin/env python3


from random import randint
from brain_games.game_engine import game_engine


def main():
    game_engine(brain_even)


def brain_even():
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


if __name__ == '__main__':
    main()
