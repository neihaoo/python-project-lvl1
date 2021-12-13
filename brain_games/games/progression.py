"""Brain Games Calc Module."""

import random

from brain_games.engine import run_game as play

MIN_PROGRESSION_LENGTH = 5
MAX_PROGRESSION_LENGTH = 10
GAME_DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(start, length, step):
    """
    Create progression.

    Args:
        start: int
        length: int
        step: int

    Returns:
        tuple
    """
    progression = ()

    while len(progression) < length:
        progression += (start, )
        start += step

    return progression


def get_random_progression():
    """
    Generate random progression.

    Returns:
        turple
    """
    start_progression = random.randint(0, 100)
    step_progression = random.randint(0, 100)
    progression_length = random.randint(
        MIN_PROGRESSION_LENGTH,
        MAX_PROGRESSION_LENGTH,
    )

    return generate_progression(
        start_progression,
        progression_length,
        step_progression,
    )


def make_question(progression, hidden_number):
    """
    Make question.

    Args:
        progression: tuple
        hidden_number: int

    Returns:
        str
    """
    question = ''

    for number in progression:
        current_element = '..' if number == hidden_number else number
        question = '{0} {1}'.format(question, current_element)

    return question.strip()


def get_game_data():
    """
    Generate game data.

    Returns:
        tuple
    """
    progression = get_random_progression()

    answer = random.choice(progression)
    question = make_question(progression, answer)

    return (question, str(answer))


def start_game():
    """
    Start the game.

    Returns:
        fn
    """
    return play(get_game_data, GAME_DESCRIPTION)
