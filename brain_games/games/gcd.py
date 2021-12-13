"""Brain Games Calc Module."""

import math
import random

from brain_games.engine import run_game as play

GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_game_data():
    """
    Generate game data.

    Returns:
        tuple
    """
    first_num = random.randint(0, 100)
    second_num = random.randint(0, 100)

    question = '{0} {1}'.format(first_num, second_num)
    answer = str(math.gcd(first_num, second_num))

    return (question, answer)


def start_game():
    """
    Start the game.

    Returns:
        fn
    """
    return play(get_game_data, GAME_DESCRIPTION)
