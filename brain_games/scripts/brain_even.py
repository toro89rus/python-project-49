#!/usr/bin/env python3


from brain_games.game_engine import game_engine
from brain_games.games.even import get_even_answers, EVEN_DESCRIPTION


def main():
    game_engine(EVEN_DESCRIPTION, get_even_answers)


if __name__ == '__main__':
    main()
