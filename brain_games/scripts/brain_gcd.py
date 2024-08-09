#!/usr/bin/env python3


from brain_games.game_engine import game_engine
from brain_games.games.gcd import get_gcd_answers, GCD_DESCRIPTION


def main():
    game_engine(GCD_DESCRIPTION, get_gcd_answers)


if __name__ == '__main__':
    main()
