from random import randint


PROGRESSION_DESCRIPTION = 'What number is missing in the progression?'
MIN_LEN = 5
MAX_LEN = 10
MIN_STEP = 1
MAX_STEP = 10
MIN_FIRST_NUM = 0
MAX_FIRST_NUM = 50


def run_progression():
    progression = []
    progression_step = randint(MIN_STEP, MAX_STEP)
    element = randint(MIN_FIRST_NUM, MAX_FIRST_NUM)
    for step_count in range(randint(MIN_LEN, MAX_LEN)):
        progression.append(str(element + step_count * progression_step))
    secret_element_index = randint(0, len(progression) - 1)
    answer = progression[secret_element_index]
    progression[secret_element_index] = '..'
    return ' '.join(progression), answer
