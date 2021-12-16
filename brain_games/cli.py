"""Brain Games CLI Module."""

import prompt


def welcome_user():
    """Greeting user."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
