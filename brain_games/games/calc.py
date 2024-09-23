from random import randint, choice

OPERATORS = ('+', '-', '*')
MIN_NUMBER = 0
MAX_NUMBER = 100
DESCRIPTION = 'What is the result of the expression?'


def get_question_and_answer() -> tuple[str, str]:
    first_num = randint(MIN_NUMBER, MAX_NUMBER)
    second_num = randint(MIN_NUMBER, MAX_NUMBER)
    operation = choice(OPERATORS)
    question = f'{first_num} {operation} {second_num}'
    match operation:
        case '+':
            correct_answer = first_num + second_num
        case '-':
            correct_answer = first_num - second_num
        case '*':
            correct_answer = first_num * second_num
    return question, str(correct_answer)
