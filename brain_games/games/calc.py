"""Brain Games Calc Module."""

import random

from brain_games.engine import run_game as play

OPERATORS = ('+', '-', '*')
GAME_DESCRIPTION = 'What is the result of the expression?'


def get_answer(left_operand, right_operand, operator):
    """
    Take two operands and operator, make an expression and calculate it.

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
    left_operand = random.randint(0, 100)
    right_operand = random.randint(0, 100)
    operator = random.choice(OPERATORS)

    question = '{0} {1} {2}'.format(left_operand, operator, right_operand)
    answer = str(get_answer(left_operand, right_operand, operator))

    return (question, answer)


def start_game():
    """
    Start the game.

    Returns:
        fn
    """
    return play(get_game_data, GAME_DESCRIPTION)
