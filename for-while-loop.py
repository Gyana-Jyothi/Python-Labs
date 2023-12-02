import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)
# Initialize a variable to control the loop
isGuessRight = False

# The loop continues until isGuessRight is True
while isGuessRight != True:
    # Prompt the user to input a guess
    guess = input("Guess a number between 1 and 10: ")

    # Check if the guessed number is equal to the target number
    if int(guess) == number:
        # If the guess is correct, print a message and set isGuessRight to True to exit the loop
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        # If the guess is incorrect, print a message and allow the user to try again in the next iteration
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

