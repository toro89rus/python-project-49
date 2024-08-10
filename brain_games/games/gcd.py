from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'

MIN_NUMBER = 1
MAX_NUMBER = 100


def get_question_and_answer():
    first_num = randint(MIN_NUMBER, MAX_NUMBER)
    second_num = randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{first_num} {second_num}'
    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num = first_num % second_num
        else:
            second_num = second_num % first_num
    return question, str(first_num + second_num)
