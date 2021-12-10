"""Brain Games Calc Module."""

from random import choice, randint

from brain_games.engine import run_game as play

PROGRESSION_LENGTH = 10

game_description = 'What number is missing in the progression?'


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
    start_progression = randint(0, 100)
    step_progression = randint(0, 100)

    progression = generate_progression(
        start_progression,
        PROGRESSION_LENGTH,
        step_progression,
    )

    answer = choice(progression)
    question = make_question(progression, answer)

    return (question, str(answer))


def start_game():
    """
    Start the game.

    Returns:
        fn
    """
    return play(get_game_data, game_description)
