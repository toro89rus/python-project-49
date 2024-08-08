#!/usr/bin/env python3

import prompt
from random import randint


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        if is_answer_correct():
            correct_answers += 1
        else:
            print(f'Let\'s try again, {name}!')
            break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')


def is_answer_correct():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    number_to_quess = randint(MIN_NUMBER, MAX_NUMBER)
    print(f'Question: {number_to_quess}')
    answer = prompt.string('Your answer: ')
    if is_even(number_to_quess):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print(f'{answer} is wrong answer ;(.'
              f'Correct answer was {correct_answer}.')
        return False


def is_even(number):
    return number % 2 == 0


if __name__ == '__main__':
    main()
