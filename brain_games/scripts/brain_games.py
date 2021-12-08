#!/usr/bin/env python

"""Brain Games main script."""

from brain_games.cli import welcome_user


def main():
    """Start games."""
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == '__main__':
    main()
