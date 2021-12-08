"""Brain Even Module."""

from secrets import randbelow

import prompt


def brain_even():
    """Brain Even Game logic."""
    name = prompt.string('May I have your name? ')

    print('Hello, {0}!'.format(name))
    print('Answer "yes" if the number is even, otherwise answer "no".')

    round_count = 3

    while round_count:
        question = randbelow(100)
        answer = 'yes' if question % 2 == 0 else 'no'

        print('Question: {0}'.format(question))

        player_answer = prompt.string('Your answer: ')

        if player_answer == answer:
            print('Correct!')

        else:
            break

        round_count -= 1

    if round_count:
        print(
            "'{0}' is wrong answer ;(. Correct answer was '{1}'.".
            format(player_answer, answer),
        )
        print("Let's try again, {0}!".format(name))
    else:
        print('Congratulations, {0}!'.format(name))
