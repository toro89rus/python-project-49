import brain_games.games.even as even
import random


def test_even_get_question_and_answer():
    random.seed(0)
    assert even.get_question_and_answer() == (50, 'yes')

    random.seed(3)
    assert even.get_question_and_answer() == (31, "no")
