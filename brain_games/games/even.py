from random import randint


MIN_NUMBER = 1
MAX_NUMBER = 100
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer() -> tuple[str, str]:
    question = randint(MIN_NUMBER, MAX_NUMBER)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return str(question), correct_answer
