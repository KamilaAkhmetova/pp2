import random

def guess_the_number():
    a = input("Hello! What is your name? ")
    print("Well, {}, I am thinking of a number between 1 and 20.".format(a))

    secret_number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        try:
            guess = int(input("Take a guess: "))

            guesses_taken += 1

            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print("Good job, {}! You guessed my number in {} guesses!".format(a, guesses_taken))
                break

        except ValueError:
            print("Please enter a valid number.")

guess_the_number()
