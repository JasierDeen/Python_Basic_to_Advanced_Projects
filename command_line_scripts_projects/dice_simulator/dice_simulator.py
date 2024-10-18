import random

def dice_simulator(num_of_dice):

    if num_of_dice <= 0:
        raise ValueError
    
    rolls = []
    for _ in range(num_of_dice):
        random_roll = random.randint(1, 6)
        rolls.append(random_roll)

    return rolls

def main():

    while True:

        try:
            user_input = input("How many dice would you like to roll ? ")

            if user_input.lower() == "exit":
                print("Thanks for playing!")
                break

            print(*dice_simulator(int(user_input)), sep=", ")
        except ValueError:
            print("Please enter a valid number")


if __name__ == "__main__":
    main()

    