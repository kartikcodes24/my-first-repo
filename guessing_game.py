import random

def number_guessing_game():
    number = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the number guessing game!")
    print("I have choosen a number between 1 and a 100.")

    while guess != number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < number:
                print("Your guess is too low")
            elif guess > number:
                print("Your guess is too high")
            else:
                print(f"You got it in {attempts} tries")
        except ValueError:
            print("Please enter a valid answer.")

if __name__ == "__main__":
    number_guessing_game()
