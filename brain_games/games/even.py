"""Brain Games Even Module."""

from random import randint

from brain_games.index import run_game

game_description = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_game_data():
    """
    Generate game data.

    Returns:
        tuple
    """
    question = randint(0, 100)
    answer = 'yes' if question % 2 == 0 else 'no'

    return (question, answer)


def start_game():
    """
    Start the game.

    Returns:
        fn
    """
    return run_game(get_game_data, game_description)
