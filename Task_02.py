import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("🎯 Welcome to the Number Guessing Game!")
    print("I've picked a number between 1 and 100. Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            difference = abs(number_to_guess - guess)

            if guess == number_to_guess:
                print(f"🎉 Congrats! You nailed it in {attempts} attempts.")
                break
            elif difference <= 5:
                print("🔥 You're very close!")
            elif guess < number_to_guess:
                print("Too low! 📉")
            else:
                print("Too high! 📈")
        except ValueError:
            print("🚫 Invalid input. Please enter a number.")

# Start the game
number_guessing_game()
