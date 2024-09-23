import brain_games.games.gcd as gcd
import random


def test_gcd_get_greatest_common_divisor():

    assert gcd.get_greatest_common_divisor(48, 18) == 6

    assert gcd.get_greatest_common_divisor(5, 15) == 5

    assert gcd.get_greatest_common_divisor(3, 3) == 3


def test_gcd_get_question_and_answer():
    random.seed(0)

    assert gcd.get_question_and_answer() == ('50 98', '2')
