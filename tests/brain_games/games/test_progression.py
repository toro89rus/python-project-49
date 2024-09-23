import brain_games.games.progression as progression
import random


def test_progression_get_question_and_answer():
    random.seed(0)
    assert progression.get_question_and_answer() == (".. 55 62 69 76 83 90 97",
                                                     '48')
