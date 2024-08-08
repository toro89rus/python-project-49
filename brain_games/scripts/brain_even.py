#!/usr/bin/env python3


from brain_games.game_engine import game_engine
from brain_games.games.even import even


def main():
    game_engine(even)


if __name__ == '__main__':
    main()
