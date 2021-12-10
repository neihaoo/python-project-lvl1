"""Brain Games Calc Module."""

from random import choice, randint

from brain_games.index import run_game

operators = ('+', '-', '*')
game_description = 'What is the result of the expression?'


def get_answer(left_operand, right_operand, operator):
    """
    Make an expression and calculates it.

    Args:
        left_operand: int
        right_operand: int
        operator: str

    Returns:
        int
    """
    if operator == '+':
        return left_operand + right_operand

    if operator == '-':
        return left_operand - right_operand

    if operator == '*':
        return left_operand * right_operand


def get_game_data():
    """
    Generate game data.

    Returns:
        tuple
    """
    left_operand = randint(0, 100)
    right_operand = randint(0, 100)
    operator = choice(operators)

    question = '{0} {1} {2}'.format(left_operand, operator, right_operand)
    answer = str(get_answer(left_operand, right_operand, operator))

    return (question, answer)


def start_game():
    """
    Start the game.

    Returns:
        fn
    """
    return run_game(get_game_data, game_description)
