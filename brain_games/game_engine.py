import prompt
from random import randint


def game_engine(game_type):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    MAX_ROUNDS = 3
    correct_answers = 0
    while correct_answers < MAX_ROUNDS:
        game_question, game_answer = game_type()
        print(f'Question: {game_question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == game_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f'{user_answer} is wrong answer ;(.'
                  f'Correct answer was {game_answer}.')
            print(f'Let\'s try again, {name}!')
            break
    if correct_answers == 3:
        print(f'Congratulations, {name}!')


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
