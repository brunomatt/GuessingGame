secret_number = 49
guess_count = 0
guess_limit = 10
guess = float()
out_of_guesses = False
valid_numbers = range(0,101)

print("Let's play a guessing game.")

while guess != secret_number and not(out_of_guesses):
    guess = float(input("Please input a number between 0 and 100. "))
    guess_count = guess_count + 1
    if guess < secret_number:
        print("Too small!  " + str(guess_limit - guess_count) + " guesses remaining."  + "  Please guess again.  ")
    elif guess > secret_number:
        print("Too big!  " + str(guess_limit - guess_count) + " guesses remaining."  + "  Please guess again.  ")
    if guess_count >= guess_limit:
        out_of_guesses = True
    if guess not in valid_numbers:
        print("Please refrain from entering decimals.")

if out_of_guesses == True:
    print("Out of guesses.  Better luck next time!")
else:
    print("Good job!  You guessed correctly!")