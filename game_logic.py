import random
from ascii_art import STAGES

# ―――――――――――――――――――――――――――――
# Globals
# ―――――――――――――――――――――――――――――

WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_MISTAKES = len(STAGES) - 1


# ―――――――――――――――――――――――――――――
# Helpers
# ―――――――――――――――――――――――――――――

def get_random_word() -> str:
    """
    Gets a random word from WORDS.
    Returns:
        str: random word
    """
    return random.choice(WORDS)


def display_game_state(mistakes: int, secret_word: str, guessed_letters: set) -> bool:
    """
    Print the current ASCII snowman stage, then show the masked word.
    Args:
        mistakes (int): number of mistakes
        secret_word (str): secret word
        guessed_letters (set): letters guessed
    Returns:
         bool: True if the player has just won, False otherwise.
    """
    print(STAGES[mistakes])

    # If not fully melted yet, show the masked word and check for win
    if mistakes < MAX_MISTAKES:
        masked = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )
        print("Word: ", masked)

        # If all letters are guessed, show the fully‐revealed word and win
        if all(letter in guessed_letters for letter in secret_word):
            print("🎉 You won! The word was:", secret_word)
            return True

        print()  # extra newline for spacing

    return False


def get_guess(guessed_letters: set) -> str:
    """
    Prompt the user for exactly one new letter (a–z) that they have not guessed yet.
    Blocks until valid.
    Args:
        guessed_letters (set): A set of letters that have been guessed yet.
    Returns:
        guess(str): the guessed letter (a-z)
    """
    while True:
        if guessed_letters:
            print("Guessed so far:", " ".join(sorted(guessed_letters)))

        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("  ▶ Please enter exactly one letter (a–z).")
        elif guess in guessed_letters:
            print(f"  ▶ You already guessed '{guess}'. Try another.")
        else:
            return guess


# ―――――――――――――――――――――――――――――
# Main game
# ―――――――――――――――――――――――――――――

def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0

    print("\nWelcome to Snowman Meltdown!\n")

    while True:
        # 1) Print current snowman + masked word (or win message)
        won = display_game_state(mistakes, secret_word, guessed_letters)
        if won:
            break

        # 2) If fully melted, it's game over
        if mistakes == MAX_MISTAKES:
            print("Game Over! The word was:", secret_word)
            break

        # 3) Otherwise, prompt for a valid new letter
        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        # 4) Update mistakes or congratulate
        if guess not in secret_word:
            mistakes += 1
            remaining = MAX_MISTAKES - mistakes + 1
            print(f"✖ '{guess}' is not in the word. Tries left: {remaining}\n")
        else:
            print(f"✓ '{guess}' is in the word!\n")

    print("\nThanks for playing!\n")


if __name__ == "__main__":
    play_game()
