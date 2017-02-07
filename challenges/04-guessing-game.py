from random import randint

def guessing_game():
    MIN = 1
    MAX = 5
    number = randint(MIN, MAX)
    is_playing = True

    while is_playing:
        guess = input("What's your guess? ")
        if int(guess) > number:
            print("Try again, lower!")
        elif int(guess) < number:
            print("Try again, higher!")
        elif int(guess) == number:
            print("You got it!")
            is_playing = False

    print("Guess a number between {} and {}".format(MIN, MAX))
    print("Delete me. Here's a random number: {}".format(number))

guessing_game()
