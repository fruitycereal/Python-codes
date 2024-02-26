#not finished!!

import random

number = str(random.randint(0,20))
print(number)

guess = int(input('You have 3 tries! Guess the secret number '))

tries = 0

while guess != number and tries < 3:
    if guess < int(number):
        print('Too small')
        tries =+ 1

    elif guess > int(number):
        print('Too big')
        tries + 1

if tries == 3:
    print('You lose bozo')

else:
    print('Correct :)')
#


secret_word = 'a lot'

guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("What's the number? ")
        guess_count += 1
        if guess != secret_word:
            print('Wrong,', guess_limit - guess_count, 'guesses left')
    else:
        out_of_guesses = True

if out_of_guesses:
    print()
    print('Out of guesses, you lose bozo')
else:
    print('Correct!')