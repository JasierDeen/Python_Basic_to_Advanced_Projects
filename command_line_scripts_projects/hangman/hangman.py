import random

word_list = ["python", "hangman", "developer", "cloud", "data", "science", "openai", "software"]

word = random.choice(word_list)
guessed_word = ["_"] * len(word) 
attempts = 6 
guessed_letters = set()

print("Welcome to Hangman!")
print(" ".join(guessed_word))
print(f"You have {attempts} attempts remaining.")

while attempts > 0:
    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter. Try again.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        for index, letter in enumerate(word):
            if letter == guess:
                guessed_word[index] = guess
        print("Good guess!")
    else:
        attempts -= 1
        print(f"Wrong guess. You have {attempts} attempts remaining.")

    print(" ".join(guessed_word))

    if "_" not in guessed_word:
        print("Congratulations! You guessed the word:", word)
        break
else:
    print("Out of attempts! The word was:", word)
