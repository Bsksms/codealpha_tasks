import random

words = ["python", "computer", "science", "program", "student"]
game_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print(" Welcome to Hangman Game!")
print("You have 6 incorrect guesses.\n")


while incorrect_guesses < max_guesses:
    
    display_word = ""
    for letter in game_word :
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word.strip())

    
    if "_" not in display_word:
        print("\nCongratulations! You guessed the word correctly.")
        break

    
    guess = input("Guess a letter: ").lower()

    
    if len(guess) != 1 or not guess.isalpha():
        print(" please enter a single alphabet.\n")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    
    if guess in game_word :
        print(" Correct guess!\n")
    else:
        incorrect_guesses += 1
        print(f" Wrong guess! Remaining attempts: {max_guesses - incorrect_guesses}\n")


if incorrect_guesses == max_guesses:
    print("\nGame Over!")
    print("The correct word was:", game_word)
    