"""Brain Games Prime Module."""

import random

from brain_games.engine import run_game as play

GAME_DESCRIPTION = (
    'Answer "yes" if given number is prime. Otherwise answer "no".'
)


def is_prime(number):
    """
    Check if a number is prime or not.

    Args:
        number: int

    Returns:
        bool
    """
    if number < 2:
        return False

    for element in range(2, number // 2 + 1):
        if number % element == 0:
            return False

    return True


def get_game_data():
    """
    Generate game data.

    Returns:
        tuple
    """
    question = random.randint(0, 100)
    answer = 'yes' if is_prime(question) else 'no'

    return (question, answer)


def start_game():
    """
    Start the game.

    Returns:
        fn
    """
    return play(get_game_data, GAME_DESCRIPTION)
