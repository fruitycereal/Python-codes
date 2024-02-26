secret_word = 'a lot'

guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("What's the secret word? ")
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
