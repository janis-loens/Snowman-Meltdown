import random
from ascii_art import STAGES



# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_MISTAKES = len(STAGES) - 1

def get_random_word():
    return random.choice(WORDS)



def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    win = False
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    if mistakes < MAX_MISTAKES :
        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )

        print("Word: ", display_word)
        if "_" not in display_word:
            print("You won! The snowman is saved!")
            win = True
        print("\n")
    return win

def get_guess(mistakes, secret_word, guessed_letters):
    while True:
        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter (a–z).")
        elif guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
        else:
            break
    return guess



def play_game():
    secret_word = get_random_word()
    guessed_letters = set()
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    while mistakes <= MAX_MISTAKES:
        win = display_game_state(mistakes, secret_word, guessed_letters)
        if win:
            break
        # Prompt user for one guess (logic to be enhanced later)
        if mistakes < MAX_MISTAKES:
            guess = get_guess(mistakes, secret_word, guessed_letters)

            guessed_letters.add(guess)
            if guess not in secret_word:
                mistakes += 1
        if mistakes == MAX_MISTAKES:
            print(STAGES[mistakes])
            print("Game Over! The word was:", secret_word)
            break







if __name__ == "__main__":
    play_game()