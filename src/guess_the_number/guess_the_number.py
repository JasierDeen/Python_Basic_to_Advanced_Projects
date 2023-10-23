from random import randint

print("")
print("---- GUESS THE NUMBER ---- \n")

start = 1
end = 100
chances = 10
found = False

secret_number = randint(start, end)

print(f"The computer chose a secret number between {start} and {end}\n")

for chance in range(chances):

    user_guess = int(input("\nGuess the number: "))
    chances -= 1
    if user_guess > 100:
        print("Your guess is greater than 100. Guess between 1 to 100")
    elif user_guess < secret_number:
        print(f"The secret number is higher than the {user_guess}")
    elif user_guess > secret_number:
        print(f"The secret number is lower than the {user_guess}")
    else:
        found = True
        print(f"Congratulations!! You found the secret number {user_guess}\n")
        break
    print(f"You have only {chances} chance/s left")

if not found:
    print(f"Hard Luck!! You haven't find the secret number {secret_number}")