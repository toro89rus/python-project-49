#!/usr/bin/env python3


from brain_games.game_engine import game_engine
from brain_games.games.calc import get_calc_answers, CALC_RULE


def main():
    game_engine(CALC_RULE, get_calc_answers)


if __name__ == '__main__':
    main()
