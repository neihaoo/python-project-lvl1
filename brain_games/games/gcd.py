"""Brain Games Calc Module."""

from math import gcd
from random import randint

from brain_games.engine import run_game as play

game_description = 'Find the greatest common divisor of given numbers.'


def find_gcd(first_num, second_num):
    """
    Find the greatest common divisor of two integers.

    Args:
        first_num: int
        second_num: int

    Returns:
        int
    """
    return gcd(first_num, second_num)


def get_game_data():
    """
    Generate game data.

    Returns:
        tuple
    """
    first_num = randint(0, 100)
    second_num = randint(0, 100)

    question = '{0} {1}'.format(first_num, second_num)
    answer = str(find_gcd(first_num, second_num))

    return (question, answer)


def start_game():
    """
    Start the game.

    Returns:
        fn
    """
    return play(get_game_data, game_description)
