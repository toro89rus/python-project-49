import brain_games.games.prime as prime
import random


def test_is_prime():

    assert prime.is_prime(-1) is False, "negative number shouldn't be prime"
    assert prime.is_prime(0) is False, "zero shouldn't be prime"
    assert prime.is_prime(1) is False, "number less than 2 shouldn't be prime"
    assert prime.is_prime(6) is False, "even number shouldn't be prime"

    assert prime.is_prime(7) is True, '7 should be prime'
    assert prime.is_prime(109) is True, '109 should be prime'


def test_prime_get_question_and_answer():
    random.seed(0)
    assert prime.get_question_and_answer() == ('50', 'no')

    random.seed(3)
    assert prime.get_question_and_answer() == ('31', "yes")
