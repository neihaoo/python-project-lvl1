"""Brain Games Engine Module."""

import prompt


def run_game(get_game_data, description):
    """
    Take game data and description and run the game.

    Args:
        get_game_data: fn
        description: str
    """
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')

    print('Hello, {0}!'.format(name))
    print(description)

    round_count = 3

    while round_count:
        (question, game_answer) = get_game_data()

        print('Question: {0}'.format(question))

        player_answer = prompt.string('Your answer: ')

        if player_answer != game_answer:
            print(
                "'{0}' is wrong answer ;(. Correct answer was '{1}'.".
                format(player_answer, game_answer),
            )
            print("Let's try again, {0}!".format(name))

            return

        print('Correct!')

        round_count -= 1

    print('Congratulations, {0}!'.format(name))
