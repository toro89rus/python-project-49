import brain_games.games.calc as calc
import random


def test_calc_get_question_and_answer():
    random.seed(0)

    assert calc.get_question_and_answer() == ("49 - 97", "-48")

    random.seed(1)

    assert calc.get_question_and_answer() == ("17 + 72", "89")

    random.seed(3)

    assert calc.get_question_and_answer() == ('30 * 75', '2250')
