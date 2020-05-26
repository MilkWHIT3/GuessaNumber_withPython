import random

guessestaken = 0
minNumber = 1
maxNumber = 20

print("Hello, guy! What´s your name?: ")
username = input()

number = random.randint(minNumber, maxNumber)
print("Well, " + username + '. I am thinking in a number between ' + str(minNumber) + ' and ' + str(maxNumber))

while guessestaken < 6:
    print("Take a guess: ")
    guess = input()
    guess = int(guess)

    guessestaken = guessestaken + 1

    if guess < number:
        print("Your guess is too low.")
    if guess > number:
        print("Your guess is too high.")
    if guess == number:
        break

if guess == number:
    guessestaken = str(guessestaken)
    print("Good job, " + username + '! You guessed my number in ' + guessestaken + ' guesses.')
if guess != number:
    number = str(number)
    print("You don't guess my number. Sorry. Try it again.")
    print("The number I was thinking of was " + number + ', by the way.')

