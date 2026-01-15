import random

def hangman():
    words = ["apple", "banana", "grape", "orange", "mango"]
    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word.")

    while attempts > 0:
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print("Word:", display_word)

        if "_" not in display_word:
            print("You won! The word was:", secret_word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in secret_word:
            attempts -= 1
            print("Wrong guess! Attempts left:", attempts)

    if attempts == 0:
        print("You lost! The word was:", secret_word)

hangman()
