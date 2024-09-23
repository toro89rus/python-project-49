from random import randint


DESCRIPTION = "What number is missing in the progression?"
PROGRESSION_MIN_LEN = 5
PROGRESSION_MAX_LEN = 11
PROGRESSION_MIN_STEP = 1
PROGRESSION_MAX_STEP = 10
MIN_FIRST_NUM = 0
MAX_FIRST_NUM = 50


def get_question_and_answer() -> tuple[str, str]:
    progression = []
    progression_step = randint(PROGRESSION_MIN_STEP, PROGRESSION_MAX_STEP)
    element = randint(MIN_FIRST_NUM, MAX_FIRST_NUM)
    progression_len = randint(PROGRESSION_MIN_LEN, PROGRESSION_MAX_LEN)
    for step_count in range(progression_len):
        progression.append(str(element + step_count * progression_step))
    secret_element_index = randint(0, len(progression) - 1)
    correct_answer = progression[secret_element_index]
    progression[secret_element_index] = ".."
    question = " ".join(progression)
    return question, correct_answer
