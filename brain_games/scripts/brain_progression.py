#!/usr/bin/env python3


from brain_games.game_engine import game_engine
from brain_games.games.progression import (run_progression,
                                           PROGRESSION_DESCRIPTION)


def main():
    game_engine(PROGRESSION_DESCRIPTION, run_progression)


if __name__ == '__main__':
    main()
