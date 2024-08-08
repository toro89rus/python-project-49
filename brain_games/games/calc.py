from random import randint, choice

OPERATORS = ('+', '-', '*')
MIN_NUMBER = 0
MAX_NUMBER = 100
CALC_RULE = 'What is the result of the expression?'


def get_calc_answers():
    first_num = randint(MIN_NUMBER, MAX_NUMBER)
    second_num = randint(MIN_NUMBER, MAX_NUMBER)
    operation = choice(OPERATORS)
    expression = f'{first_num} {operation} {second_num}'
    match operation:
        case '+':
            correct_answer = str(first_num + second_num)
        case '-':
            correct_answer = str(first_num - second_num)
        case '*':
            correct_answer = str(first_num * second_num)
    return expression, correct_answer
