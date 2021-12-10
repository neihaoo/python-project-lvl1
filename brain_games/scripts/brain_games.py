#!/usr/bin/env python

"""Brain Games Welcome Script."""

from brain_games.games.cli import welcome_user


def main():
    """Start the games."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
