"""Brain Games Even Module."""

import random

from brain_games.engine import run_game as play

GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_data():
    """
    Generate game data.

    Returns:
        tuple
    """
    question = random.randint(0, 100)
    answer = 'yes' if question % 2 == 0 else 'no'

    return (question, answer)


def start_game():
    """
    Start the game.

    Returns:
        fn
    """
    return play(get_game_data, GAME_DESCRIPTION)
