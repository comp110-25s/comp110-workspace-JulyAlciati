"""My First Wordle Game in class COMP110!"""

__author__: str = "730715920"


def contains_char(word: str, letter_guessed: str) -> bool:
    """Check if a letter guessed is in the word"""
    assert len(letter_guessed) == 1, f"len('{letter_guessed}') is not 1"
    i = 0

    while i < len(word):
        if letter_guessed == word[i]:
            return True
        i += 1

    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Create colored emojis for characters."""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    i = 0
    emoji: str = ""
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        elif contains_char(secret, guess[i]) is True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
        i += 1
    return emoji


def input_guess(word_length: int) -> str:
    """Generate a prompt for entering a word with specifed length."""

    word = input(f"Enter a {word_length} character word: ")

    while len(word) != word_length:
        word = input(f"That wasn't {word_length} chars! Try again: ")

    return word


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turns = 0
    guess = ""
    color = ""

    while turns < 6 and guess != secret:
        turns += 1
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret))
        color = emojified(guess=guess, secret=secret)

        print(color)

    if guess == secret:
        print(f"You won in {turns}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")

print(main)
